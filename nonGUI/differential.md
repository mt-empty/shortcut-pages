# Differential

> Source: https://en.wikipedia.org/wiki/Differentiation_rules

> Aliases: differentiation, differentiation-rules, derivatives

$ Linearity of Differentiation
    `H(x) = aF(x) + bG(x)          {{H'(x) = aF'(x) + bG'(x)}} 
    `(aF(x))'                      {{aF'(x)}} 
    `(F(x) + G(x))'                {{F'(x) + G'(x)}} 
    `(F(x) - G(x))'                {{F'(x) - G'(x)}} 

$ Product Rule
    `H(x) = F(x)*G(x)              {{H'(x) = F'(x)*G(x) + F(x)*G'(x)}} 

$ Chain Rule
    `H(x) = F( G(x) )              {{H'(x) = F'( G(x) )*G'(x)}} 

$ Inverse Function Rule
    `(F⁻¹)'(x)                     {{1 / F'(F⁻¹(x))}} 

$ Elementary Power Rule
    `F(x) = xⁿ                     {{F'(x) = nxⁿ⁻¹}} 

$ Reciprocal Rule
    `H(x) = 1 / F(x)               {{H'(x) = -F'(x) / (F(x))²}} 

$ Quotient Rule
    `(F(x) / G(x))'                {{(F'(x)G(x) - F(x)G'(x)) / (G(x))²}} 

$ Generalized Power Rule
    `(F(x)ᴳ⁽ˣ⁾)'                   {{(F(x)ᴳ⁽ˣ⁾)(F'(x)G(x) / F(x) + G'(x)ln(F(x)))}} 
    `xᵃ                            {{axᵃ⁻¹}} 

$ Exponential and Logarithmic Functions
    `(cᵃˣ)'                        {{cᵃˣaln(c) where c > 0}} 
    `(eᵃˣ)'                        {{aeᵃˣ}} 
    `(logₘx)'                      {{1 / (xln(m)) where m > 0 and m ≠ 1}} 
    `(ln x)'                       {{1 / x}} 
    `(xˣ)'                         {{xˣ(1 + ln x)}} 

$ Trignometric Functions
    `(sin x)'                      {{cos x}} 
    `(cos x)'                      {{-sin x}} 
    `(tan x)'                      {{sec² x or 1 + (tan(x))²}} 
    `(sec x)'                      {{(sec x)(tan x)}} 
    `(cosec x)'                    {{-(cosec x)(cot x)}} 
    `(cot x)'                      {{-cosec² x}} 
    `(asin x)'                     {{1 / √(1 - x²)}} 
    `(acos x)'                     {{-1 / √(1 - x²)}} 
    `(atan x)'                     {{1 / (1 + x²)}} 
    `(asec x)'                     {{1 / (|x|√(x² - 1))}} 
    `(acosec x)'                   {{-1 / (|x|√(x² - 1))}} 
    `(acot x)'                     {{-1 / (1 + x²)}} 

$ Hyperbolic Functions
    `(sinh x)'                     {{cosh x}} 
    `(cosh x)'                     {{sinh x}} 
    `(tanh x)'                     {{sech² x}} 
    `(sech x)'                     {{-(sech x)(tanh x)}} 
    `(cosech x)'                   {{-(cosech x)(coth x)}} 
    `(coth x)'                     {{-cosech² x}} 
    `(asinh x)'                    {{1 / √(x² + 1)}} 
    `(acosh x)'                    {{1 / √(x² - 1)}} 
    `(atanh x)'                    {{1 / (1 - x²)}} 
    `(asech x)'                    {{-1 / (x√(1 - x²))}} 
    `(acosech x)'                  {{-1 / (|x|√(x² + 1))}} 
    `(acoth x)'                    {{1 / (1 - x²)}} 

