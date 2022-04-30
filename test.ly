dashPlus = "trill"
voice_one = {
  r8 r8 a'8 a' c''4. c''4. e'16 e' e' e' d'8 d'8 e'8 c'2 r8 d'8 d'8 a'8 a' e'8 c''4. c''4. d'8 d'8 r8 r8 e'8 r8 r8 r8 r8 
}
voice_two =  {
  r8 r8 a'8 a' e'8 c''4. c'4 e'16 e' e' e' d'8 d'8 e'8 r8 r8 r8 r8 e'8 r8 a'8 a' e'8 e'8 c'4 c''4. c''4. d'8 d'8 e'8 r8 r8 r8 r8 
}
voice_three = {
  r8 r8 d'8 d'8 e'8 c''4. c'4 e'16 e' e' e' d'8 d'8 r8 r8 r8 d'8 d'8 e'8 r8 a'8 a' e'8 e'8 c''4. c''4. d'8 d'8 r8 r8 a'8 a' r8 r8 r8
}
% voice_four =  {
%   d'8 d'8 r8 r8 e'8 r8 d'8 d'8 e'8 r8 e'8 r8 a'8 a' r8 c'4 d'8 d'8 e'8 d'8 d'8 e'8 r8 d'8 d'8 r8 e'8 r8 r8 r8 r8 a'8 a' e'8 r8 a'8 a' r8 e'8 a'8 a'
% }
{
  \version "2.22.2"
  % \time 4/4
  <<
    \new Staff {
      \voice_one
    }
    \new Staff {
      \voice_two
    }
    \new Staff {
      \clef bass 
      \voice_three
    }
    % \new Staff {
    %   \voice_four
    % }
  >>
}