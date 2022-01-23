def start(
        self,
        zeit_max         = 100,
        zeit_intervall   = 0.1,
        zuruecksetzen    = True):
        
        if zuruecksetzen:
            self.zuruecksetzen()
        
        
        """
            Dokumentation zur Funktion 'linspace':
                - https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
                - Gibt Zahlen in gleichmaessigen Abstand ueber ein spezifiziertes Intervall aus.
        """
        # Array fuer Zeitintervalle
        t = np.linspace(0, zeit_max, int( zeit_max / zeit_intervall )  + 1)
        
        # temporaere Listen
        S = self.s
        E = self.e
        I = self.i
        R = self.r
        
        # temporaere Parameter
        alpha = self.alpha
        beta  = self.beta
        gamma = self.gamma
        rho   = self.rho
        zeit_intervall    = t[1] - t[0]
        
        # Schleife zur Berechnung (siehe Kapitel SEIR-Modell)
        for _ in t[1:]:
            next_S = S[-1] - ( (1 - rho) * beta *S[-1] * I[-1] ) * zeit_intervall
            next_E = E[-1] + ( (1 - rho) * beta *S[-1] * I[-1] - alpha * E[-1]) * zeit_intervall
            next_I = I[-1] + ( alpha * E[-1] - gamma*I[-1]) * zeit_intervall
            next_R = R[-1] + ( gamma * I[-1]) * zeit_intervall
            
            S.append(next_S)
            E.append(next_E)
            I.append(next_I)
            R.append(next_R)
        
        """
            Dokumentation zur Funktion 'linspace':
                - https://numpy.org/doc/stable/reference/generated/numpy.stack
                - Fuegt die Arrays zusammen.
        """
        # 'Einsammeln' der Ergebnisse
        ergebnis = np.stack([S, E, I, R]).T
        self.s = S
        self.e = E
        self.i = I
        self.r = R
        
        # Schreiben der finalen Werte in das Array
        self.vals_ = [self.s[-1], self.e[-1], self.i[-1], self.r[-1]]
        
        return ergebnis