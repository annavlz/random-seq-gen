\version "2.22.2"
% automatically converted by musicxml2ly from part3.musicxml
\pointAndClickOff

\header {
    encodingsoftware =  "Sibelius 22.3.0"
    encodingdate =  "2022-05-03"
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
    short-indent = 2.423076923076923\cm
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative d'' {
    \clef "treble" \time 16/4 \key c \major \pageBreak | % 1
    \stemDown d2 -\markup{ \small {part3} } \stemDown c2 r4 \stemDown d2.
    r16 \stemDown d16 [ \stemDown d8 ] \stemDown b2. r8 \stemDown b8 r8
    \stemDown c8 r16 \stemUp ais16 r8 r4 \bar "|."
    }

PartPTwoVoiceOne =  \relative bes'' {
    \clef "treble" \time 16/4 \key c \major \pageBreak | % 1
    r8 -\markup{ \small {part3a} } \stemDown bes8 \stemDown as8 r8
    \stemDown bes8 [ \stemDown as8 ] r8 \stemDown as8 \stemDown bes8 r8
    \stemDown a8 [ \stemDown a8 ] r8 \stemDown a8 \stemDown a8 r8
    \stemDown gis8 [ \stemDown gis8 ] r8 \stemDown ais8 \stemDown b8 [
    \stemDown b8 ] \stemDown gis8 r8 \stemDown a8 [ \stemDown fis8
    \stemDown fis8 \stemDown fis8 ] r8 \stemDown fis8 \stemDown f4 \bar
    "|."
    }

PartPThreeVoiceOne =  \relative a'' {
    \clef "treble" \time 16/4 \key c \major \transposition c \pageBreak
    | % 1
    \stemDown a16 [ -\markup{ \small {part3b} } \stemDown as16 \stemDown
    g16 \stemDown as16 ] \stemDown g16 [ \stemDown ges16 ] r16 \stemDown
    f16 \stemDown ges16 [ \stemDown g16 ] r16 \stemDown as16 r16
    \stemDown a16 [ \stemDown g8 ] \stemDown fis16 [ \stemDown fis16
    \stemDown fis16 \stemDown fis16 ] \stemDown fis16 [ \stemDown g16 ]
    r8 r16 \stemDown a16 r16 \stemDown a16 r16 \stemDown a16 [ \stemDown
    f8 ] \stemDown a16 [ \stemDown a16 ] r16 \stemDown a16 \stemDown a16
    [ \stemDown a16 ] r8 r16 \stemDown a16 r16 \stemDown a16 r16
    \stemDown a16 [ \stemDown f8 ] \stemDown a16 [ \stemDown a16
    \stemDown a16 \stemDown a16 ] \stemDown a16 [ \stemDown a16 ] r16 r16
    r16 \stemDown a16 r16 \stemDown a16 r16 \stemDown a16 [ \stemDown f8
    ] \bar "|."
    }

PartPFourVoiceOne =  \relative a' {
    \clef "treble" \time 16/4 \key c \major \pageBreak | % 1
    \stemUp a16 [ -\markup{ \small {part3c} } \stemUp a16 \stemUp a16
    \stemUp a16 ] \stemUp a16 [ \stemUp a16 ] r8 r16 \stemUp a16 r16
    \stemUp a16 r16 \stemUp a16 [ \stemUp f8 ] r1 r1 r1 \bar "|."
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
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
            \new Staff
            <<
                \set Staff.instrumentName = "P2"
                \set Staff.shortInstrumentName = "Vc."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoVoiceOne" {  \PartPTwoVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "P3"
                \set Staff.shortInstrumentName = "Db."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPThreeVoiceOne" {  \PartPThreeVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = " "
                \set Staff.shortInstrumentName = " "
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFourVoiceOne" {  \PartPFourVoiceOne }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
    }

