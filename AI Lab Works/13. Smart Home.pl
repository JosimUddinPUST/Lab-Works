% Predicate to get all necessary inputs from the user
get_user_inputs(CurrentTemp, DesiredTemp, TimeOfDay, HomeOccupied) :-
    write('Enter the current temperature: '),
    read(CurrentTemp),
    write('Enter the desired temperature: '),
    read(DesiredTemp),
    write('Enter the time of day (morning/afternoon/evening/night): '),
    read(TimeOfDay),
    write('Is the home occupied? (yes/no): '),
    read(HomeOccupied).

% Rule to check if heating is needed based on inputs
activate_heating(Current, Desired, Occupied) :-
    Current < Desired,
    Occupied = yes,
    write('Heating activated.').

% Rule to check if cooling is needed based on inputs
activate_cooling(Current, Desired, Occupied) :-
    Current > Desired,
    Occupied = yes,
    write('Cooling activated.').

% Rule to reduce energy usage at night when unoccupied
reduce_energy(TimeOfDay, Occupied) :-
    TimeOfDay = night,
    Occupied = no,
    write('Energy usage reduced for unoccupied night time.').

% Rule to maintain comfort range if occupied
maintain_comfort(Current, Desired, Occupied) :-
    Occupied = yes,
    (Current < 18; Current > 24),
    (Current < Desired -> activate_heating(Current, Desired, Occupied) ; activate_cooling(Current, Desired, Occupied)).

% Start program by getting user input and checking conditions
start :-
    get_user_inputs(CurrentTemp, DesiredTemp, TimeOfDay, HomeOccupied),
    (   activate_heating(CurrentTemp, DesiredTemp, HomeOccupied)
    ->  true
    ;   activate_cooling(CurrentTemp, DesiredTemp, HomeOccupied)
    ->  true
    ;   reduce_energy(TimeOfDay, HomeOccupied)
    ->  true
    ;   maintain_comfort(CurrentTemp, DesiredTemp, HomeOccupied)
    ->  true
    ;   write('No action needed.'), nl
    ).
