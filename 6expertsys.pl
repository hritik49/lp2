% Facts
punctual(yes).
targets_met(yes).
team_player(yes).
takes_initiative(no).

% Rules
excellent_performance :-
    punctual(yes),
    targets_met(yes),
    team_player(yes),
    takes_initiative(yes).

good_performance :-
    punctual(yes),
    targets_met(yes),
    team_player(yes),
    takes_initiative(no).

needs_improvement :-
    punctual(no),
    targets_met(no).

% Query to evaluate performance
evaluate_performance :-
    (excellent_performance -> 
        write('Excellent Performance');
    good_performance -> 
        write('Good Performance');
    needs_improvement -> 
        write('Needs Improvement');
    write('Performance could not be evaluated.')).