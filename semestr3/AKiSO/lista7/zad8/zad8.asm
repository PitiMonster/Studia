                org $1000

start  
   LDA #0	; 8 bardziej znaczących bitów dzielnej
   STA TH
  
   LDA #200	; 8 mniej znaczących bitów dzielnej	
   STA TLQ
   
   LDA #1	; bitowy dzielnik	
   STA B
   
   LDA TH
   LDX #8
   ASL TLQ	; tlq *= 2
L1 ROL @	; A = A*2 + C
   BCS L2	; jeśli wypanie 1 to C = 1 i robimy jump do L2
   CMP B	;
   BCC L3	; if (B > A)
L2 SBC B	; odejmujemy A -= B 
   SEC		; ustawienie C na 1 jeśli jest 0	
L3 ROL TLQ	; dodanie na mniej znaczące bity dzielnej jedynki bo wiemy że liczba jest podzielna jeśli A > B było
   DEX		; X--
   BNE L1	; if x > 0 jump L1
   
   LDY TLQ 	;
   
TH dta b(0)	; na końcu y = wynik dzielenia a A = reszta
TLQ dta b(0)
B dta b(0)
text	equ *
	org $2E0
	dta a(start)
	end of file
