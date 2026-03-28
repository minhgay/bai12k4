import streamlit as st
st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')
with st.sidebar:
    st.title('Vương quốc mô hình')
    st.header('Chào mừng bạn đến với vương quốc mô hình')
    st.write('Chúng tôi bán các loại mô hình cao cấp ...')
    st.image('hinh1.jpg')
    st.write('house: Địa chỉ:')
    st.write('phone:Điện thoại')
st.title("Vương quốc mô hình ")
chu_de = ['Dragon ball','Naruto','One piece']
cols = st.columns(len(chu_de))
choose = None
for i,cd in enumerate(chu_de):
    with cols[i]:
        if st.button(cd):
            choose= cd
if choose:
    st.header(f'Danh sách mô hình{choose}')
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            st.image('hinh1.jpg',caption=f'MS: 00{i+1}')
st.header('delivery')
with st.form('delivery bill'):
    loai = st.selectbox('chu de',chu_de)
    ma = st.selectbox('Mã số', ['001', '002', '003'])
    slg = st.slider('Số lượng', 0, 10, 0)
    name = st.text_input('Họ tên:')
    sdt = st.text_input('SĐT:')
    add = st.text_input('Địa chỉ:')
    bill = {'Mô hình': loai,
            'Mã số': ma,
            'Số lượng': slg,
            'Họ tên KH': name,
            'SĐT': sdt,
            'Địa chỉ': add}
    if st.form_submit_button('Xác nhận'):
        st.header('Bạn đã chọn:')
        for k, v in bill.items():
            st.write(k, v)
    # In hóa đơn
    if st.checkbox('In hoá đơn'):
        hoa_don = '\n'.join([f"{k}: {v}" for k, v in bill.items()])
        st.download_button('Tải hoá đơn', hoa_don)
