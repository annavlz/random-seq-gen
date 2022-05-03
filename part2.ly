\version "2.22.2"
% automatically converted by musicxml2ly from part2.musicxml
\pointAndClickOff

\header {
    encodingsoftware =  "Sibelius 22.3.0"
    encodingdate =  "2022-05-02"
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
    short-indent = 0.4405594405594406\cm
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative a, {
    \clef "bass" \numericTimeSignature\time 4/4 \key c \major \pageBreak
    | % 1
    \stemUp a2 \stemUp b2 | % 2
    r4 \stemUp b2. \break | % 3
    r16 \stemUp a16 [ \stemUp a8 ] \stemUp b2. | % 4
    r8 \stemUp b8 r8 \stemUp f8 r16 \stemUp a16 [ \stemUp b16 ] r16 r4
    \bar "|."
    }

PartPTwoVoiceOne =  \relative bes, {
    \clef "bass" \numericTimeSignature\time 4/4 \key c \major \pageBreak
    | % 1
    r8 \stemUp bes8 \stemUp as8 r8 \stemUp bes8 [ \stemUp as8 ] r8
    \stemUp as8 | % 2
    \stemUp a8 r8 \stemUp a8 [ \stemUp a8 ] r8 \stemUp bes8 \stemUp as8
    r8 \break | % 3
    \stemUp as8 [ \stemUp as8 ] r8 \stemUp bes8 \stemUp b8 [ \stemUp b8
    ] \stemUp as8 r8 | % 4
    \stemUp a8 [ \stemUp ges8 \stemUp ges8 \stemUp ges8 ] r8 \stemUp ges8
    \stemUp f4 \bar "|."
    }

PartPThreeVoiceOne =  \relative a, {
    \clef "bass" \numericTimeSignature\time 4/4 \key c \major
    \transposition c \pageBreak | % 1
    \stemUp a16 [ \stemUp a16 \stemUp a16 \stemUp a16 ] \stemUp a16 [
    \stemUp a16 ] r16 r16 r16 \stemUp a16 r16 \stemUp a16 r16 \stemUp a16
    [ \stemUp f8 ] | % 2
    \stemUp a16 [ \stemUp a16 \stemUp a16 \stemUp a16 ] \stemUp a16 [
    \stemUp a16 ] r16 r16 r16 \stemUp a16 r16 \stemUp a16 r16 \stemUp a16
    [ \stemUp f8 ] \break | % 3
    \stemUp a16 [ \stemUp a16 \stemUp a16 \stemUp a16 ] \stemUp a16 [
    \stemUp a16 ] r16 r16 r16 \stemUp a16 r16 \stemUp a16 r16 \stemUp a16
    [ \stemUp f8 ] | % 4
    \stemUp a16 [ \stemUp a16 \stemUp a16 \stemUp a16 ] \stemUp a16 [
    \stemUp a16 ] r16 r16 r16 \stemUp a16 r16 \stemUp a16 r16 \stemUp a16
    [ \stemUp f8 ] \bar "|."
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
                \set Staff.instrumentName = "Violoncello"
                \set Staff.shortInstrumentName = "Vc."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoVoiceOne" {  \PartPTwoVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Double Bass"
                \set Staff.shortInstrumentName = "Db."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPThreeVoiceOne" {  \PartPThreeVoiceOne }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
    }

