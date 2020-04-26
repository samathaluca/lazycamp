travis 

[![Build Status](https://travis-ci.org/samathaluca/lazycamp.svg?branch=master)](https://travis-ci.org/samathaluca/lazycamp)


Database plan. 

MODEL/ DB FIELDS (rows)

CAMPING SPOTS

id: INT
title: STR
Pitch type: STR (rural/ town/ airport/ farm/ river/ seaside/ beach/ cliff)
Pitch mood : STR (relaxed/ vibrant/ solitude)
Owner type : STR (friendly/ remote/)
Extras offered : STR ( collection from public transport, washing, breakfast, kit hire)
Utilities on pitch : STR
Utilities nearby : STR
(Amenities on pitch : STR)
Amenities nearby : STR
Parking or public transport details : STR
Address: STR
Description: TEXT
Price: FLOAT
Photo_main: STR
Photo_1: STR
Photo_2: STR
Photo_3: STR
Photo_4: STR
Photo_5: STR
Total pitches available: STR
Good choice for: STR (families, young couples, early birds, nightowls, nature lovers, wild swimming)
Is late arrival: Boolean
Is 24 hours: Boolean
Full Set up available: INT[0] (default of zero)
Year of set up: INT

Owner name: STR
Owner photo: STR
Owner Description: STR
Owner Phone: INT
Owner email : STR

General Contact enquiries
id: INT
(user_id: INT)
name: STR
message: TEXT
email: INT
Phone: INT

SPOT Specific Contact enquiries
id: INT
user_id: INT
camping spot: STR
camping spot id: INT
name: STR
message: TEXT
email: INT
Phone: INT
date: DATE

USER 
name: STR
visits: STR
Favourite Spot: STR
Bio: TEXT








