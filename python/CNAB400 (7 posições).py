fout=open('Resultado da análise.txt','w')# Definição de funçõesdef verificaAGCONTA(k,a,b,banco):    if a==b==0:        num = k        N = num[:-1]        S = 0        for i in range(1,len(N)+1):            m = int(N[-i])            S = S + m*(i+1)        d = 11 - S%11        if banco == '001':            if d == 10:                d = 'X'            elif d == 11:                d = '0'        N=str(d)        if N != num[-1]:            fout.write('Agência/Conta inválida\n')    elif a==b==banco==0:        num = k        N = num[:-1]        S = 0        for i in range(1,len(N)+1):            m = int(N[-i])            S = S + m*(i+1)        d = 11 - S%11        N=str(d)        if N != num[-1]:            fout.write('Dígito verficador inválido\n')    elif a!=b:        num = L[k][a-1:b]        N = num[:-1]        S = 0        for i in range(1,len(N)+1):            m = int(N[-i])            S = S + m*(i+1)        d = 11 - S%11        if banco == '001':            if d == 10:                d = 'X'            elif d == 11:                d = '0'        N=str(d)        if N != num[-1]:            fout.write('Posições %d a %d: Valor esperado - %s; Valor encontrado - %s\n'%(a,b,num[:-1]+str(d),num))def verificaCNPJ(k,a,b):    if a==b==0:        CNPJ = k        N=CNPJ[:-2]        for k in range(0,2):            S = 0            for i in range(1,9):                m = int(N[-i])                S = S + m*(i+1)            if len(N)>8:                for j in range(1,len(N)-7):                    m = int(N[-j-8])                    S = S + m*(j+1)            d = 11 - S%11            if d == 10:                d = 0            elif d == 11:                d = 0            N = N + str(d)        if N[-2:] != CNPJ[-2:]:            fout.write('CNPJ inválido\n')    elif a!=b:        CNPJ = L[k][b-14:b]        N=CNPJ[:-2]        if N.isdigit()==False:            fout.write('Posições %d a %d: Valor esperado - Valores numéricos; Valor encontrado - %s\n'%(b-13,b,CNPJ))        else:            for k in range(0,2):                S = 0                for i in range(1,9):                    m = int(N[-i])                    S = S + m*(i+1)                if len(N)>8:                    for j in range(1,len(N)-7):                        m = int(N[-j-8])                        S = S + m*(j+1)                d = 11 - S%11                if d == 10:                    d = 0                elif d == 11:                    d = 0                N = N + str(d)            if N[-2:] != CNPJ[-2:]:                fout.write('Posições %d a %d: Valor esperado - %s; Valor encontrado - %s\n'%(b-13,b,N,CNPJ))def verificaCPF(k,a,b):    if a==b==0:        CPF = k        N = CPF[:-2]        S = 0        for i in range(1,10):            m = int(N[i-1])            S = S + m*(i)        d = S%11        if d == 10:            d = 0        elif d == 11:            d = 0        N = N + str(d)        S=0        for i in range(0,10):            m = int(N[i])            S = S + m*(i)        d = S%11        if d == 10:            d = 0        elif d == 11:            d = 0        N = N + str(d)        if N!=CPF:            fout.write('CPF inválido\n')    if a!=b:        CPF = L[k][b-11:b]        N = CPF[:-2]        S = 0        if N.isdigit()==False:            fout.write('Posições %d a %d: Valor esperado - Valores numéricos; Valor encontrado - %s\n'%(b-10,b,CPF))        else:            for i in range(1,10):                m = int(N[i-1])                S = S + m*(i)            d = S%11            if d == 10:                d = 0            elif d == 11:                d = 0            N = N + str(d)            S=0            for i in range(0,10):                m = int(N[i])                S = S + m*(i)            d = S%11            if d == 10:                d = 0            elif d == 11:                d = 0            N = N + str(d)            if N!=CPF:                fout.write('Posições %d a %d: Valor esperado - %s; Valor encontrado - %s\n'%(b-10,b,N,CPF))def verificaCART(k):    if k not in ['11','12','17','31','51']:        fout.write('Carteira inválida. Utilize, 11,12,17,31 ou 51\n')def verificaTamanho(k,a):    if len(k)!= a:        fout.write('Formato invalido - o registro deve conter %d posições\n'%a)        def compara(k,a,b,J):    if len(J)==1:        if a<b and L[k][a-1:b] not in J:            fout.write('Posições %d a %d: Valor esperado - '%(a,b)+ str(J) +'; Valor encontrado - %s\n'%L[k][a-1:b])        elif a==b and L[k][a-1] not in J:            fout.write('Posição %d: Valor esperado - '%a+ str(J)+'; Valor encontrado - %s\n'%L[k][a-1:b])    elif len(J)>1:        if a<b and L[k][a-1:b] not in J:            fout.write('Posições %d a %d: Valores esperados - '%(a,b)+ str(J) +'; Valor encontrado - %s\n'%L[k][a-1:b])        elif a==b and L[k][a-1] not in J:            fout.write('Posição %d: Valores esperados - '%a+ str(J)+'; Valor encontrado - %s\n'%L[k][a-1:b])def verificaTipo(k,a,b,tipo):    if tipo=='digit':        if L[k][a-1:b].isdigit()==False:            fout.write('Posições %d a %d: Valores esperados - valores numéricos; Valores encontrados - %s\n'%(a,b,L[k][a-1:b]))    if tipo=='name':        if L[k][a-1:b]==' '*len(L[k][a-1:b]):                fout.write('Posições %d a %d: Valores esperados - valores alfanuméricos; Valores encontrados - %s\n'%(a,b,L[k][a-1:b]))def verificaTipoDigit(k,a,b):    if L[k][a-1:b].isdigit()==True:        return True    else:        return False                def verificaNome(k,a,b,nome):        if nome.upper() not in L[k][a-1:b].upper():            fout.write('Posições %d a %d: Valor esperado - %s; Valor encontrado - %s\n'%(a,b,nome,L[k][a-1:b]))def verificaData(k,a,b):    if L[k][a+1:a+3] not in ['01','02','03','04','05','06','07','08','09','10','11','12']:        fout.write('Posições %d a %d: Valores esperados - [01,02,03,04,05,06,07,08,09,10,11,12]; Valor encontrado - %s\n'%(a+1,a+2,L[k][a+1:a+3]))    elif L[k][a+1:a+3] in ['01','03','05','07','08','10','12'] and (int(L[k][a-1:a+1])>31 or int(L[k][a-1:a+1])==0):        fout.write('Posições %d a %d: Valores esperados - entre 01 e 31; Valor encontrado - %s\n'%(a-1,a,L[k][a-1:a+1]))    elif L[k][a+1:a+3] in ['02','04','06','09','11'] and (int(L[k][a-1:a+1])>30 or int(L[k][a-1:a+1])==0):        fout.write('Posições %d a %d: Valores esperados - entre 01 e 30; Valor encontrado - %s\n'%(a-1,a,L[k][a-1:a+1]))def verificaHora(k,a,b):    if int(L[k][a-1:a+1])>24:        fout.write('Posições %d a %d: Valores esperados - entre 00 e 24; Valor encontrado - %s\n'%(a,a+1,L[k][a-1:a+1]))    if int(L[k][a+1:a+3])>59:        fout.write('Posições %d a %d: Valores esperados - entre 00 e 59; Valor encontrado - %s\n'%(a+2,a+3,L[k][a+1:a+3]))    if int(L[k][a+3:a+5])>59:        fout.write('Posições %d a %d: Valores esperados - entre 00 e 59; Valor encontrado - %s\n'%(a+4,a+5,L[k][a+3:a+5]))def verificaCodBarras(k,a,b):    A=L[k][a-1:b]    B = A[0:4] + '0' + A[5:44]    S = int(B[0])*4 + int(B[1])*3 +int(B[2])*2 + int(B[3])*9    for i in range(13,53,8):        for j in range(9,1,-1):            S = S + int(B[i-j])*j    d = 11- S%11    if d==0 or d==10 or d==11:        d = 1    else:        d = d    B = A[0:4] + str(d) + A[5:44]    if str(d) != A[4]:        fout.write('Posições %d a %d: Valor esperado: %s - Valor encontrado: %s\n'%(a,b,B,A))#Declaração de variáveiscontHL=0contDetalheAB=0contDetalheJ=0somaA=0somaJ=0CNPJint = int(input('CNPJ: '))verificaCNPJ(str(CNPJint).zfill(14),0,0)CNPJstr = str(CNPJint).zfill(14)CPFint = int(input('CPF: '))verificaCPF(str(CPFint).zfill(11),0,0)CPFstr = str(CPFint).zfill(14)CONVint = int(input('Convênio: '))CONVstr = str(CONVint).zfill(9)AGstr = input('Agência: ').zfill(6).upper()verificaAGCONTA(AGstr,0,0,'001')CONTAstr = input('Conta: ').zfill(13).upper()verificaAGCONTA(CONTAstr,0,0,'001')NOME_CONV = input('Nome: ').upper()CARTint = int(input('Carteira: '))CARTstr = str(CARTint)verificaCART(CARTstr)VARint = int(input('Variação: '))VARstr = str(VARint).zfill(3)verificaAGCONTA(VARstr,0,0,0)MOD = int(input('Modalidade (1 - Simples; 2 - Vinculada; 3 - Descontada; 4 - Vendor): '))TIPO_CONV = str(input('Tipo de convênio (1,2,3,4 ou 5): '))print('\n')#Importação e leitura do arquivoL=open('CNAB400.txt', 'r').readlines()#Início da validaçãofor x in range (0,len(L)):    #Registro Header     if L[x][0] =='0':        H=x        contDetalheAB+=1        fout.write('Registro Header:\n')        verificaTamanho(L[x],401)        compara(x,2,2,'1')        compara(x,3,9,'REMESSA')        compara(x,10,11,'01')        compara(x,12,19,'COBRANCA')        compara(x,20,26,'       ')        compara(x,27,30,AGstr[1:5])        compara(x,31,31,AGstr[5].upper())        compara(x,32,39,CONTAstr[4:12])        compara(x,40,40,CONTAstr[12].upper())        compara(x,41,46,'000000')        compara(x,47,76,NOME_CONV.ljust(30))        compara(x,77,94,['001BANCODOBRASIL  ','001BANCO DO BRASIL'])        verificaData(x,95,100)        verificaTipo(x,101,107,'digit')        compara(x,108,129,'                      ')        compara(x,130,136,CONVstr[2:])        compara(x,137,394,'                                                                                                                                                                                                                                                                  ')        compara(x,395,400,str(contDetalheAB).zfill(6))        fout.write('\n')#Registro Detalhe:    if L[x][0]=='7':        D7=x        contDetalheAB+=1        fout.write('Registro Detalhe:\n')        verificaTamanho(L[x],401)        compara(x,2,3,['01','02'])        if L[x][1:3]=='01':            compara(x,4,17,CPFstr)        elif L[x][1:3]=='02':            compara(x,4,17,CNPJstr)        compara(x,18,21,AGstr[1:5])        compara(x,22,22,AGstr[5].upper())        compara(x,23,30,CONTAstr[4:12])        compara(x,31,31,CONTAstr[12].upper())        compara(x,32,38,CONVstr[2:])        verificaTipo(x,39,63,'name')        if TIPO_CONV in ['4','5']:            compara(x,64,70,CONVstr[2:])            verificaTipo(x,71,80,'digit')        compara(x,81,82,'00')        compara(x,83,84,'00')        compara(x,85,87,'   ')        compara(x,88,88,[' ','A'])        compara(x,89,91,'   ')        compara(x,92,94,VARstr)        compara(x,95,95,'0')        compara(x,96,101,'000000')        if MOD == 1:            compara(x,102,106,'     ')        elif MOD == 2:            compara(x,102,106,'02VIN')        elif MOD == 3:            compara(x,102,106,'04DSC')        elif MOD == 4:            compara(x,102,106,'08VDR')        compara(x,107,108,CARTstr)        compara(x,109,110,['01','02','03','04','05','06','07','08','09','10','11','12','16','31','32','33','34','35','36','37','38','39','40'])        verificaTipo(x,111,120,'name')        verificaData(x,121,126)        verificaTipo(x,127,139,'digit')        compara(x,140,142,'001')        compara(x,143,146,'0000')        compara(x,147,147,' ')        compara(x,148,149,['01','02','03','05','08','09','10','12','13','15','25','26','27'])        compara(x,150,150,['N','A'])        verificaData(x,151,156)        if L[x][108:110]=='01':            compara(x,157,158,['00','01','03','04','05','10','15','20','25','30','45','06','07','22'])            compara(x,159,160,['00','01','03','04','05','10','15','20','25','30','45','06','07','22'])        elif L[x][108:110]=='02':            compara(x,157,158,['42','44','46'])            compara(x,159,160,['42','44','46'])        elif L[x][108:110]=='09':            compara(x,157,158,['00','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','35','40','45'])            compara(x,159,160,['00','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','35','40','45'])        verificaTipo(x,161,173,'digit')        if L[x][108:110]=='01' and L[x][101:106] =='08VDR':            verificaData(x,174,179)            verificaTipo(x,180,184,'digit')            verificaTipo(x,185,189,'digit')            compara(x,190,190,['0','1'])            compara(x,191,192,'00')        elif L[x][108:110] in ['35','36']:            compara(x,174,174,['1','2','9'])            if L[x][173] in ['1','2']:                verificaData(x,175,180)            elif L[x][173]=='9':                compara(x,175,180,'000000')            verificaTipo(x,181,192,'digit')        elif L[x][108:110] in ['38','39']:            if L[x][108:110]=='38':                compara(x,174,176,'000')            elif L[x][108:110]=='39':                verificaTipo(x,174,176,'digit')            compara(x,177,192,'0000000000000000')        elif L[x][108:110]=='16':            compara(x,174,174,['1','2'])            compara(x,175,180,'000000')            verificaTipo(x,181,192,'digit')        elif L[x][156:158]=='31':            verificaData(x,174,179)            verificaTipo(x,180,192,'digit')        else:            verificaTipo(x,174,192,'digit')        if L[x][106:108]=='12':            verificaTipo(x,193,204,'digit')            compara(x,205,205,['1','2','3','4','5','6','7'])        else:            compara(x,193,205,'0000000000000')        verificaTipo(x,206,218,'digit')        compara(x,219,220,['00','01','02'])        if L[218:220]=='00':            verificaTipo(x,221,234)        elif L[218:220]=='01':            verificaCPF(x,221,234)        elif L[218:220]=='02':            verificaCNPJ(x,221,234)        verificaTipo(x,235,271,'name')        compara(x,272,274,'   ')        verificaTipo(x,275,314,'name')        verificaTipo(x,315,326,'name')        verificaTipo(x,327,334,'digit')        verificaTipo(x,335,349,'name')        compara(x,350,351,['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'])        if L[x][87]==' ':            verificaTipo(x,352,391,'name')        elif L[x][87]=='A':            if L[x][373:377]=='CNPJ':                verificaTipo(x,352,372,'name')                compara(x,373,373,' ')                verificaCNPJ(x,378,391)            elif L[x][377:380]=='CPF':                verificaTipo(x,352,376,'name')                compara(x,377,377,' ')                verificaCPF(x,381,391)            else:                fout.write('Para posição 88 preenchida com "A", utilize "CNPJ" nas posições 374 a 377 ou "CPF" nas posições 378 a 380.\n')        if (L[x][108:110]=='01' and L[x][156:158]=='06') or (L[x][108:110]=='01' and L[x][158:160]=='06'):             compara(x,392,393,['06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','35','40'])        compara(x,394,394,' ')        compara(x,395,400,str(contDetalheAB).zfill(6))        fout.write('\n')        #Registro Detalhe Tipo 5 - Multa:    if L[x][0]=='5' and L[x][1:3] == '99':        D599=x        contDetalheAB+=1        fout.write('Registro Detalhe Tipo 5 - Multa:\n')        verificaTamanho(L[x],401)        compara(x,4,4,['1','2','9'])        if L[x][3] in ['1','2']:            verificaData(x,5,10)        elif L[x][3]==['9']:            compara(x,5,10,'000000')        compara(x,23,394,' '*372)        compara(x,395,400,str(contDetalheAB).zfill(6))            fout.write('\n')#Registro Detalhe Tipo 5 - email:    if L[x][0]=='5' and L[x][1:3] == '01':        D501=x        contDetalheAB+=1        fout.write('Registro Detalhe Tipo 5 - email:\n')        verificaTamanho(L[x],401)        verificaTipo(x,4,139,'name')        compara(x,140,394,' '*255)                                                               compara(x,395,400,str(contDetalheAB).zfill(6))            fout.write('\n')        #Registro Detalhe Tipo 5 - Número do titulo do cedente com 15 posições:    if L[x][0]=='5' and L[x][1:3] == '03':        D503=x        contDetalheAB+=1        fout.write('Registro Detalhe Tipo 5 - email:\n')        verificaTamanho(L[x],401)        verificaTipo(x,4,18,'name')        compara(x,19,394,' '*376)                                                              compara(x,395,400,str(contDetalheAB).zfill(6))            fout.write('\n')        #Registro Trailer de Arquivo:    if L[x][0]=='9':        T=x        contDetalheAB+=1        fout.write('Registro Trailer:\n')        verificaTamanho(L[x],401)        compara(x,1,1,'9')        compara(x,2,394,393*' ')        compara(x,395,400,str(contDetalheAB).zfill(6))        fout.write('\n')        fout.close()Fim = input('Tecle ENTER para finalizar')        