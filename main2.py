import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('streamlit 入門編')

st.write('プログレスバー')
'start!!'

latest_iteration = st.empty()
bar= st.progress(0)

for i in range(100):
    latest_iteration.text(f'interation{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

'done'

# left_column,right_column = st.beta_columns(2)
# left_column.button('右カラムに文字を表示')

# expander = st.beta_expandar('dgddddddd')
# expander.write('dgdg')
text = st.text_input(
    'あなたの趣味を足得てください',
   
)
con = st.slider('あなたの今の調子は',0,100,50)


'あなたの趣味',text
'コンンディション：', con

if st.checkbox('show Image'):
    img =Image.open('nowards.png')
    st.image(img,caption='kohei imanishi ', use_column_width = True)

st.write('DataFrame')

df = pd.DataFrame({
    '1列目' : [1,2,3,4],
    '2列目' : [10,20,30,40]
})

st.table(df)

"""
# 章
## 節
### 港

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""