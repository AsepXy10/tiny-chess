import json,os,urllib.request as u
E=os.getenv("MAKEFUN_ENV_URL")
KN=(33,31,18,14,-14,-18,-31,-33)
DG=(15,17,-15,-17)
OG=(1,-1,16,-16)
Q=[x for x in range(128)if x&15<8]
CF=(0,1,2,3,3,2,1,0)
B=bytearray(128);S=0;C=0;P=-1;K=[0,0];N=0
U=[]
KL=[0]*64
KP=bytearray([15])*128;KP[0]=13;KP[7]=14;KP[4]=12;KP[112]=7;KP[119]=11;KP[116]=3
M=9999
A=Exception
def sq(n):return chr(97+(n&7))+chr(49+(n>>4))
def uc(m):
 p=(m>>14)&7
 return sq(m&127)+sq((m>>7)&127)+('nbrq'[p-2]if p else'')
def fn(f):
 global S,C,P,QN
 B[:]=b'\0'*128
 w=f.split();QN=0;q=112;e=w[3]
 for ch in w[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   p='PNBRQK'.index(ch.upper())+1
   p+=6*(ch>'Z')
   B[q]=p;QN+=p%6==5
   if p%6==0:K[p//6-1]=q
   q+=1
 S=w[1]=='b'
 C=sum(1<<'KQkq'.find(c)for c in w[2]if c!='-')
 P=-1 if e=='-' else 16*ord(e[1])+ord(e[0])-881
def at(s,by):
 for O,v in(((32*by-17,32*by-15),1),(KN,2),(OG+DG,6)):
  for d in O:
   t=s+d
   if not t&0x88 and B[t]==v+6*by:return 1
 for d in DG+OG:
  t=s+d
  while not t&0x88:
   p=B[t]
   if p:
    if p-6*by in((3,5)if d in DG else(4,5)):return 1
    break
   t+=d
 return 0
def pp(s,t2,ms):
 ms.append(s|(t2<<7)|((5 if(s>>4)==6-5*S else 0)<<14))
def gn(cp):
 ms=[]
 for s in Q:
  p=B[s]
  if not p or(p>6)!=S:continue
  t=p-6*(p>6)
  if t==1:
   d=16-32*S
   for dd in(d,d-1,d+1):
    t2=s+dd
    if t2&0x88:continue
    q=B[t2]
    if dd==d:
     if q:continue
     if(s>>4)==6-5*S:pp(s,t2,ms)
     elif not cp:
      ms.append(s|(t2<<7))
      if(s>>4)==1+5*S and not B[s+2*d]:ms.append(s|((s+2*d)<<7))
    elif q and(q>6)!=S:pp(s,t2,ms)
    elif t2==P and not q:ms.append(s|(t2<<7))
  else:
   for d in(0,0,KN,DG,OG,DG+OG,OG+DG)[t]:
    t2=s+d
    while not t2&0x88:
     q=B[t2]
     if q:
      if(q>6)!=S:ms.append(s|(t2<<7))
      break
     if not cp:ms.append(s|(t2<<7))
     if t in(2,6):break
     t2+=d
 if not cp:
  for b,k,e,r in((1,4,6,7),(2,4,2,0),(4,116,118,119),(8,116,114,112)):
   if C&b and not any(B[min(k,r)+1:max(k,r)])and all(not at(x,1-S)for x in(k,(k+e)//2,e)):ms.append(k|(e<<7))
 return ms
def mk(m):
 global S,C,P,QN
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 pc=B[f];cp=B[t];es=-1
 if pc%6==1 and t==P and not cp:
  es=t-16+32*S;B[es]=0
 U.append((m,cp,es,C,P))
 B[f]=0
 B[t]=pr+6*S if pr else pc
 QN+=pr==5
 QN-=cp%6==5
 if pc%6==0:
  K[S]=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0
  elif f-t==2:B[t+1]=B[t-2];B[t-2]=0
 C&=KP[f]&KP[t]
 P=(f+t)//2 if pc%6==1 and abs(t-f)==32 else -1
 S^=1
def un():
 global S,C,P,QN
 m,cp,es,C,P=U.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 pc=B[t]
 B[f]=pc if not pr else 7-6*S
 B[t]=cp
 if es>=0:B[es]=1+6*S
 QN-=pr==5
 QN+=cp%6==5
 if pc%6==0:
  K[S^1]=f
  if t-f==2:B[t+1]=B[t-1];B[t-1]=0
  elif f-t==2:B[t-2]=B[t+1];B[t+1]=0
 S^=1
def ev():
 s=0
 for x in Q:
  p=B[x]
  if not p:continue
  w=p<7;t=p-6+6*w;r=x>>4;f=x&7
  if not w:r=7-r
  c=CF[f]+CF[r]
  if t==1:v=100+6*r
  elif t==2:v=300+6*c
  elif t==3:v=322+4*c
  elif t==4:v=500
  elif t==5:v=894+2*c
  elif QN:v=-15*r
  else:v=8*c-24
  s+=v if w else -v
 return s if S==0 else -s
def od(ms,pl):
 ms.sort(key=lambda m:1000+B[(m>>7)&127]%6*10-B[m&127]%6 if B[(m>>7)&127]else(m==KL[pl]),reverse=True)
 return ms
def sr(d,a,b,pl):
 global N;N+=1
 if N>90000:raise A
 if d==0:
  if pl>40:return ev()
  s=ev()
  if s>=b:return s
  a=max(a,s)
 best=-M;lg=0
 for m in od(gn(not d),pl):
  mv=S;mk(m)
  if at(K[mv],S):un();continue
  lg+=1
  s=-sr(max(d-1,0),-b,-a,pl+1);un()
  if s>best:best=s
  a=max(a,s)
  if a>=b:KL[pl]=m;break
 if not lg:return a if d==0 else-M+pl if at(K[S],S^1)else 0
 return best if d else a
def root(fen,legal):
 global N
 fn(fen);N=0;best=0
 for d in range(1,13):
  a=-M;b=M;bs=-M;bm=0
  try:
   for m in od(gn(0),0):
    mv=S;mk(m)
    if at(K[mv],S):un();continue
    s=-sr(d-1,-b,-a,1);un()
    if s>bs:bs=s;bm=m
    a=max(a,s)
  except A:break
  if bm:best=bm
 r=uc(best)
 return r if r in legal else legal[0]
while 1:
 g=json.load(u.urlopen(E+'/game',b'{}'))
 if g['status']=='done':break
 g=json.load(u.urlopen(E+'/move',json.dumps({'game':g['game'],'move':root(g['fen'],g['legal_moves'])}).encode()))
