import streamlit as st
import json
import os
import random
from collections import defaultdict

# --- 配置 ---
# 更新为包含五个文件路径
FILE_PATHS = [
    '/Users/juno/Desktop/results/wirting_zh_pair_merge_1k_3epoch_副本.json',
    '/Users/juno/Desktop/results/wirting_zh_pair_merge_5k_3epoch_副本.json',
    '/Users/juno/Desktop/results/wirting_zh_pair_merge_10k_3epoch_副本.json',
    '/Users/juno/Desktop/results/wirting_zh_pair_merge_origin_3epoch_副本.json',
    '/Users/juno/Desktop/results/wirting_zh_pair_merge_baseline_3epoch_副本.json'
]

# --- 辅助函数 ---

@st.cache_data
def load_and_preprocess_data():
    """
    加载并预处理指定的JSON文件，将相同question_id的条目合并。
    """
    merged_data = {}
    
    for file_path in FILE_PATHS:
        if not os.path.exists(file_path):
            st.error(f"错误: 文件 '{file_path}' 不存在，请检查路径。")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for qid, content in data.items():
                if qid not in merged_data:
                    merged_data[qid] = {
                        "question_id": qid,
                        "prompt": content.get("prompt", ""),
                        "my_responses": []
                    }
                
                my_response_text = content.get("my_response")
                if my_response_text:
                    merged_data[qid]["my_responses"].append({
                        "source_file": os.path.basename(file_path),
                        "text": my_response_text
                    })
        except Exception as e:
            st.error(f"处理文件 '{file_path}' 时发生错误: {e}")

    # 过滤掉响应数量不为5的条目，确保每组都有5个结果可比较
    filtered_data = [item for item in merged_data.values() if len(item["my_responses"]) == 5]
    if len(filtered_data) < len(merged_data):
        st.warning(f"注意: 已自动过滤掉 {len(merged_data) - len(filtered_data)} 个响应数量不为5的条目。")

    return filtered_data

def initialize_session():
    """初始化会话状态变量。"""
    if "data" not in st.session_state:
        st.session_state.data = load_and_preprocess_data()
        st.session_state.current_index = 0
        st.session_state.rankings = defaultdict(dict)
        st.session_state.max_index = len(st.session_state.data) - 1
        st.session_state.last_shuffled_index = -1
        st.session_state.shuffled_responses_for_display = []


def get_ranked_data_as_json():
    """
    将当前已标注的排名数据转换为JSON字符串。
    """
    qid_to_index = {item['question_id']: i for i, item in enumerate(st.session_state.data)}
    
    rankings_list = []
    for qid, data in st.session_state.rankings.items():
        sequence_number = qid_to_index.get(qid, -1) + 1
        rankings_list.append({
            "sequence_number": sequence_number,
            "question_id": qid,
            **data
        })
        
    rankings_list.sort(key=lambda x: x['sequence_number'])
    
    # 提醒：根据您的个性化设置，这里使用了 ensure_ascii=False
    return json.dumps(rankings_list, indent=4, ensure_ascii=False)

# --- Streamlit 应用程序主函数 ---
st.set_page_config(layout="wide")
st.title("AI 回复排名工具 (顺序阅读版)")

with st.spinner('正在加载和处理数据...'):
    initialize_session()

if not st.session_state.data:
    st.warning("没有可供处理的数据。请检查文件路径和内容。")
    st.stop()

# --- 侧边栏 ---
st.sidebar.header("操作")

# 跳转功能
st.sidebar.markdown("---")
st.sidebar.subheader("跳转到")
with st.sidebar.form(key="jump_form"):
    jump_to = st.number_input(
        "输入要跳转到的条目编号:",
        min_value=1,
        max_value=st.session_state.max_index + 1,
        value=st.session_state.current_index + 1 if st.session_state.current_index <= st.session_state.max_index else st.session_state.max_index + 1,
        step=1,
        key="jump_input"
    )
    if st.form_submit_button("跳转"):
        target_index = jump_to - 1
        if 0 <= target_index <= st.session_state.max_index:
            st.session_state.current_index = target_index
            st.rerun()
        else:
            st.sidebar.error("输入的编号无效！")

st.sidebar.markdown("---")

# --- 主要修改点：将所有下载按钮逻辑统一到侧边栏 ---
if not st.session_state.rankings:
    st.sidebar.info("完成第一条标注后即可在此处导出。")
else:
    is_finished = st.session_state.current_index > st.session_state.max_index
    if is_finished:
        st.sidebar.download_button(
            label="✅ 下载全量排名结果",
            data=get_ranked_data_as_json(),
            file_name="ranked_results_all.json",
            mime="application/json",
            key="download_all_sidebar",
            type="primary" # 使用醒目样式
        )
    else:
        st.sidebar.download_button(
            label="导出当前已标注的结果",
            data=get_ranked_data_as_json(),
            file_name=f"ranked_results_partial_{len(st.session_state.rankings)}_items.json",
            mime="application/json",
            key="download_partial"
        )


# --- 主界面 ---
is_finished_main = st.session_state.current_index > st.session_state.max_index

if not is_finished_main:
    progress_text = f"进度: {st.session_state.current_index + 1}/{st.session_state.max_index + 1}"
    progress_value = (st.session_state.current_index) / st.session_state.max_index if st.session_state.max_index > 0 else 0
    st.progress(progress_value, text=progress_text)

    current_item = st.session_state.data[st.session_state.current_index]

    if st.session_state.current_index != st.session_state.last_shuffled_index:
        shuffled_list = current_item['my_responses'][:]
        random.shuffle(shuffled_list)
        st.session_state.shuffled_responses_for_display = shuffled_list
        st.session_state.last_shuffled_index = st.session_state.current_index

    display_responses = st.session_state.shuffled_responses_for_display
    response_options = [f"回复 {chr(65 + i)}" for i in range(len(display_responses))]
    option_to_response_map = {opt: resp for opt, resp in zip(response_options, display_responses)}

    st.subheader(f"数据条目 {st.session_state.current_index + 1} / {st.session_state.max_index + 1}")
    st.markdown("---")
    
    st.markdown(f"**Question ID:** `{current_item['question_id']}`")
    st.markdown("**Prompt:**")
    st.info(current_item['prompt'])

    with st.form(key=f"ranking_form_{st.session_state.current_index}", clear_on_submit=True):
        st.markdown("**请阅读以下五个回复:**")
        
        for i, response in enumerate(display_responses):
            st.markdown(f"#### {response_options[i]}")
            with st.container(border=True, key=f"response_container_{st.session_state.current_index}_{i}"):
                st.write(response['text'])

        st.markdown("---") 

        st.markdown("**请为每个排名分配一个回复:**")
        rank1_choice = st.radio("**第一名**", response_options, index=None, key=f"rank1_{st.session_state.current_index}", horizontal=True)
        rank2_choice = st.radio("**第二名**", response_options, index=None, key=f"rank2_{st.session_state.current_index}", horizontal=True)
        rank3_choice = st.radio("**第三名**", response_options, index=None, key=f"rank3_{st.session_state.current_index}", horizontal=True)
        rank4_choice = st.radio("**第四名**", response_options, index=None, key=f"rank4_{st.session_state.current_index}", horizontal=True)
        rank5_choice = st.radio("**第五名**", response_options, index=None, key=f"rank5_{st.session_state.current_index}", horizontal=True)
        
        if st.form_submit_button("提交排名并进入下一组", type="primary"):
            choices = [rank1_choice, rank2_choice, rank3_choice, rank4_choice, rank5_choice]
            if None in choices:
                st.error("请为每个排名都选择一个回复。")
            elif len(set(choices)) != 5:
                st.error("每个回复只能被选择一次，请检查您的选择。")
            else:
                ranked_responses = []
                for rank, choice_label in enumerate(choices, 1):
                    original_response = option_to_response_map[choice_label]
                    ranked_responses.append({
                        "rank": rank,
                        "source_file": original_response['source_file'],
                        "my_response": original_response['text']
                    })

                st.session_state.rankings[current_item['question_id']] = {
                    "prompt": current_item['prompt'],
                    "ranked_responses": ranked_responses
                }
                
                if st.session_state.current_index == st.session_state.max_index:
                    st.toast("🎉 太棒了！这是最后一条，结果已成功保存。", icon="✅")
                
                st.session_state.current_index += 1
                st.rerun()

    # 导航按钮 (在表单外部)
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("⬅️ 上一条", disabled=(st.session_state.current_index <= 0)):
            st.session_state.current_index -= 1
            st.rerun()
    with col_nav2:
        if st.button("跳过，进入下一条 ➡️", disabled=(st.session_state.current_index >= st.session_state.max_index)):
            st.session_state.current_index += 1
            st.rerun()

else:
    # 完成界面
    st.success("所有条目已完成排名！")
    st.balloons()
    st.info("您现在可以从左侧的侧边栏下载完整的排名结果。")