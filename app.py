
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quan ly diem sinh vien",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Tao du lieu 10 sinh vien
data = {
    "Ho_ten": [
        "Nguyen Van An", "Tran Thi Binh",
        "Le Van Cuong", "Pham Thi Dung",
        "Hoang Van Em", "Vu Thi Giang",
        "Do Van Hung", "Bui Thi Lan",
        "Ngo Van Minh", "Dang Thi Nga"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 5, 9, 7, 8],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 4, 8, 7, 6],
    "Cuoi_ky": [9, 8, 7, 9, 6, 9, 5, 9, 8, 7]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# 3. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Hien thi bang diem
st.subheader("1. Bảng điểm sinh viên")

bang = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang, use_container_width=True)

# 5. Thong ke
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_dat = int((df["Tong_ket"] >= 5).sum())

st.subheader("2. Thống kê")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình", f"{df['Tong_ket'].mean():.2f}")
c2.metric("Điểm cao nhất", f"{sv_max['Tong_ket']:.2f}")
c3.metric("Điểm thấp nhất", f"{sv_min['Tong_ket']:.2f}")
c4.metric("Số sinh viên đạt", str(so_dat))

st.write("Sinh viên cao nhất:", sv_max["Ho_ten"])
st.write("Sinh viên thấp nhất:", sv_min["Ho_ten"])

# 6. Chon sinh vien
st.subheader("3. Tra cứu sinh viên")

ten = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Họ tên:", sv["Ho_ten"])
st.write("Điểm chuyên cần:", sv["Chuyen_can"])
st.write("Điểm giữa kỳ:", sv["Giua_ky"])
st.write("Điểm cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", sv["Tong_ket"])
st.write("Xếp loại:", sv["Xep_loai"])

# 7. Ve bieu do
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_ylim(0, 10)

plt.xticks(rotation=45, ha="right")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 8. Thong tin nguoi tao
st.divider()
st.caption("NGUYỄN VIỆT TRIẾT | MSSV:051207014168 ")
