import qrcode

upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MASSAGE

#defining the pament URL based on the UPI ID and the pament app
#You can modify these URLs based on the pament apps you want to support

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#creat QR code for each pament app

phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the QR code to image file (optional)

phonepay_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the QR code 
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()
