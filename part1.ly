\version "2.22.2"
% automatically converted by musicxml2ly from part1.musicxml
\pointAndClickOff

\header {
    encodingsoftware =  "Sibelius 22.3.0"
    encodingdate =  "2022-05-01"
    encoder =  "Duncan Haynes"
    encodingdescription =  "Sibelius / MusicXML 3.0"
    }

#(set-global-staff-size 20.0)
\paper {
    
    paper-width = 21.0\cm
    paper-height = 29.7\cm
    top-margin = 1.49\cm
    bottom-margin = 1.49\cm
    left-margin = 1.49\cm
    right-margin = 1.49\cm
    between-system-space = 2.1\cm
    indent = 1.6153846153846154\cm
    short-indent = 1.6153846153846154\cm
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative f' {
    \clef "treble" \time 8/4 \key c \major \pageBreak | % 1
    r8 \stemUp f8 \stemUp d4 \stemDown b'16 [ \stemDown cis16 ] r8 r16
    \stemUp g16 r16 \stemUp g16 r16 \stemUp g16 r8 \stemUp a4 \stemUp e2
    \bar "|."
    }


% The score definition
\score {
    <<
        
        \new Staff
        <<
            \set Staff.instrumentName = " "
            \set Staff.shortInstrumentName = " "
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
    }

