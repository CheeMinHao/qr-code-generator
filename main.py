import qrcode
import streamlit as st
from io import BytesIO


def main():
        st.title("QR Code Generator")
        url_input = st.text_input("Please insert your URL link here")
        qr_name = st.text_input("Please insert your desired file name")
        generate_qr = st.button("Generate QR Code")
        if generate_qr:
                create_qr_code(url_input, qr_name)

def create_qr_code(url_input, qr_name):

        enable_download = False

        #Creating an instance of qrcode
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        try:
                qr.add_data(url_input)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
        except:
                st.error("Invalid Link provided, please try again.")

        enable_download = True
        if enable_download:
                buf = BytesIO()
                img.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.image(byte_im, width=300)
                st.download_button(label="Download Your QR Code", data=byte_im, file_name=f'{qr_name}.png', mime="image/png")

if __name__ == "__main__":
        main()