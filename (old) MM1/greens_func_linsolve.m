% symbolic green's function calculation
clear; clc;

syms x z real


X = exp(z) ;
Y = exp(-2*z) ;
V = exp(sym(3)) ;

Xa = exp(x) ;
Ya = exp(-2*x) ;
Va = exp(sym(3)) ;

W = [ -X + Y, X + (1/2) * V * Y ;
    - X - 2 * Y, X - V*Y] ;
rhs = [0; 1] ;

solved = linsolve (W, rhs) ;

A = solved(1,1) ;
C = solved (2,1);


Gl = A * ( Xa - Ya) ;
Gr = C* (Xa + (0.5)*Va*Ya) ;

Gl_simplified = simplify(subs(Gl, [X,Y], [exp(z), exp(-2*z)]));
Gr_simplified = simplify(subs(Gr, [X,Y], [exp(z), exp(-2*z)]));

f = 3*sin(z);
I_left  = int( Gr * f, z, 0, x );       % 0..x uses right branch (x>z)
I_right = int( Gl * f, z, x, 1 );       % x..1 uses left branch  (x<z)
y = simplify(I_left + I_right);

% plot it 

fplot(matlabFunction(y,'Vars',x), [0,1], 'LineWidth', 1.8); grid on
xlabel('x'); ylabel('y(x)');
title('Solution y(x) for f(x)=3 sin x via Green''s function (symbolic)');
