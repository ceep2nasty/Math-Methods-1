% MM1 HW9 P2

x = [-3 -2.5 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 2.5 3]';
y = [28.58 24.05 13.24 10.29 3.27 2.65 1.21 3.81 5.99 12.39 17.02 27.16 34.42]';

% Fit to y = ax^2 + ...

X1 = [ones(size(x)) x x.^2];
sol1 = X1\y ;

a1= sol1(1) ;
b1= sol1(2);
c1= sol1(3);

% add cubic term

X2 = [ones(size(x)) x x.^2 x.^3];

sol2 = X2\y ;

a2= sol2(1) ;
b2= sol2(2) ;
c2= sol2(3) ; 
d2= sol2(4) ; 

% Compute residuals
y1 = a1 + b1*x + c1*x.^2 ;
y2 = a2 + b2*x + c2*x.^2 + d2*x.^2 ;

r1 = abs(y-y1) ;
r2 = abs(y-y2) ;

aveR1 = mean(r1) ;
aveR2 = mean(r2) ;iupg

