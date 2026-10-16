import numpy as np, wave, sys
SR=44100; T=15.0; N=int(SR*T); rng=np.random.default_rng(7)
L=np.zeros(N); R=np.zeros(N)
def add(sig,t0,g=1.0,pan=0.0):
    i=int(t0*SR); n=min(len(sig),N-i)
    if n<=0: return
    L[i:i+n]+=sig[:n]*g*(1-max(pan,0)); R[i:i+n]+=sig[:n]*g*(1+min(pan,0))
def tt(d): return np.arange(int(d*SR))/SR
def kick(g=1):
    t=tt(0.28); f=50+90*np.exp(-t*28); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*11)
def hat():
    t=tt(0.06); n=rng.standard_normal(len(t)); n=np.diff(n,prepend=0); return n*np.exp(-t*70)*0.5
def clap():
    t=tt(0.18); n=rng.standard_normal(len(t)); n=np.convolve(n,np.ones(3)/3,'same'); return n*np.exp(-t*25)*0.6
def click():
    t=tt(0.09); return (np.sin(2*np.pi*1800*t)*np.exp(-t*60)+0.4*np.sin(2*np.pi*900*t)*np.exp(-t*45))*0.9
def pop():
    t=tt(0.22); return np.sin(2*np.pi*(300+500*np.exp(-t*30))*t)*np.exp(-t*14)*0.8
def whoosh(d=0.45,up=True):
    t=tt(d); n=rng.standard_normal(len(t)); k=np.ones(40)/40
    f=np.convolve(n,k,'same'); env=(np.sin(np.pi*np.clip(t/d,0,1))**2); return f*env*(1.4)
def hit():
    t=tt(0.7); return (np.sin(2*np.pi*(45+60*np.exp(-t*18))*t)*np.exp(-t*5)+0.3*rng.standard_normal(len(t))*np.exp(-t*30))*1.0
def bass(f,d=0.5):
    t=tt(d); return np.sin(2*np.pi*f*t)*np.exp(-t*3.5)*(1-np.exp(-t*80))*0.55
def tick(f=1500):
    t=tt(0.04); return np.sin(2*np.pi*f*t)*np.exp(-t*90)*0.35
B=0.5
for b in range(30):
    t=b*B
    if t>=1.0 or b==0:   # nhịp kick bắt đầu sau cú bấm
        pass
    if 1.0<=t<14.0 or t>=14.5: add(kick(),t,0.55 if t<8.5 else 0.8)
    if t>=3.0 and t<13.5: add(hat(),t+B/2,0.35,0.3)
    if t>=6.0 and t<13.5 and b%2==1: add(clap(),t,0.45)
    if t>=8.0 and t<13.5: add(bass([55,55,65.4,49][b%4]),t,0.6)
# tiếng động theo sự kiện
add(click(),1.0,0.8)                 # bấm nút
add(pop(),1.5,0.5)                   # nút co thành chấm
add(whoosh(0.4),2.6,0.5,-0.3)        # chấm nhảy sang biểu đồ
add(pop(),3.5,0.6)                   # hạ cánh
for k,tk in enumerate([4.1,4.7]): add(tick(1200+k*300),tk,0.5)
add(pop(),5.0,0.45)                  # khung callout
add(whoosh(0.45),5.7,0.7,0.3)        # chấm bắn dọc đường
add(hit(),6.5,0.7)                   # đĩa phủ khung
add(click(),7.0,0.5)                 # hình vuông
add(click(),7.55,0.5)                # viên thuốc
add(whoosh(0.5),8.0,0.6,-0.2)        # thu về chấm
for k in range(5): add(tick(1000+k*180),8.6+k*0.4,0.4)
add(whoosh(0.7),9.9,0.8,0.2)         # vòng chữ mở
add(hit(),10.9,0.5)                  # lật nền sang đen
add(pop(),11.9,0.55)                 # chấm đứng cuối ngay.
add(whoosh(0.6),13.55,0.6,-0.3)      # quay về
add(pop(),14.6,0.4)
# hạ nhạc đầu và cuối để vòng lặp liền, nén nhẹ
env=np.ones(N); fi=int(0.02*SR); env[:fi]=np.linspace(0,1,fi); env[-fi:]=np.linspace(1,0,fi)
L*=env; R*=env
m=max(np.abs(L).max(),np.abs(R).max()); L/=m/0.8; R/=m/0.8
x=np.stack([L,R],1); x=(np.clip(x,-1,1)*32767).astype('<i2')
w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(x.tobytes()); w.close()
print('xong', sys.argv[1])
