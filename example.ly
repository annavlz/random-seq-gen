dashPlus = "trill"
voice_one = \relative a' {
  d16 d16 d16 d16 b8 d16 d16 b8 a4 c4 d4 r8 r8 r8 d16 d16 a4 c4 d4
}
voice_two =  \relative a' {
  a4 c4 d4 r8 r8 d16 d16 r8 d16 d16 d16 d16 d16 d16 b8 a4 c4 d4 
}
% voice_three = {
%   r8 r8 d'8 d'8 e'8 c''4. c'4 e'16 e' e' e' d'8 d'8 r8 r8 r8 d'8 d'8 e'8 r8 a'8 a' e'8 e'8 c''4. c''4. d'8 d'8 r8 r8 a'8 a' r8 r8 r8
% }

{
  \version "2.22.2"
  <<
    \new Staff {
      \voice_one
    }
    \new Staff {
      \voice_two
    }
    % \new Staff {
    %   \clef bass 
    %   \voice_three
    % }
  >>
}