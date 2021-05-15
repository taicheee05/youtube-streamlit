import numpy as np
import streamlit as st
import pandas as pd

st.title('Streamlit 超入門')
st.write('DataFrame')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]    
})
st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""

df1=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c'])

st.dataframe(df1)

st.line_chart(df1)

df2=pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],
                 columns=['lat','lon'])
st.map(df2)

from PIL import Image

if st.checkbox('show image'):
    video_file = open('/Users/mt199/Dropbox/勉強_趣味/動画/統計/1新規/統計学のための最低限数学/自然対数の底と極限/ネイピア数.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

option = st.selectbox(
    'あたなの好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です'

st.write('Interactiveなwidget')
text_widget = st.text_input('あなたの趣味を教えてください')

'あなたの趣味:',text_widget

st.write('スライダー')
condition = st.slider('あなたの今の調子は？',0,10,5)
'あなたの今の調子は？',condition

st.write('Interactiveなwidget_sidebar')
text_widget_sidebar = st.sidebar.text_input('あなたの趣味を教えてください_sidebar')

'あなたの趣味_slider:',text_widget_sidebar

st.write('スライダー_sidebar')
condition_sidebar = st.sidebar.slider('あなたの今の調子は？_sidebar',0,10,5)
'あなたの今の調子は_slider？',condition_sidebar


left_column,right_column=st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
expander1=st.beta_expander('問い合わせ')
expander1.write('問い合わせ内容を書く')

import time

st.write('プログレスバーの表示')
'Start!!'
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


expander2=st.beta_expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander3=st.beta_expander('問い合わせ')
expander3.write('問い合わせ内容を書く')
