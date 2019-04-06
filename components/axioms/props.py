old_label_pattern = "[a-zA-Z0-9_]*$"
dest_key_pattern = "[a-zA-Z0-9_].*(-[a-zA-Z0-9_].*)?"
label_pattern = "^[a-zA-Z0-9_]{2,2048}$"
invalid_label_pattern = "^[.]{2,2048}$"
pg_data = {
  'max_syllables': 5,
  'syllables':['Af','Al','Ael','Baf','Bel','Ber','Berd','Bes','Bo','Bor','Bran','Bru','Car','Chor','Cig','Cla','Da','Do','Doh','Don','Dor','Dre','Dreb','Eg','Feg','Er','Es','Ev','Fal','Ful','Fan','Fen','Far','Fum','Ga','Gahn','Gaith','Gar','Gen','Glen','Go','Gram','Ha','Hag','Harg','Ho','Ig','Ka','Kar','Kra','Krac','Ky','Lag','Lap','Le','Lef','Lis','Lo','Lu','Mal','Mar','Me','Mez','Mich','Mil','Mul','Mo','Mun','Mus','Ned','Nic','No','Nor','Nu','Os','Pal','Pen','Phil','Po','Poy','Pos','Pus','Pres','Quas','Que','Rag','Ralt','Ram','Rin','Ron','Ris','Ro','Sa','See','Ser','Sur','Sho','Sit','Spor','Tar','Tas','Ten','Ton','To','Tra','Treb','Tred','Tue','Vak','Ven','Web','Wil','Yor','Zef','Zell','Zen','Zo'],
  'vowels': ['a','e','i','o','u','y'],
  'vowel_pattern': '[aieouyAIEOUY]',
  'suffices': ['of the North','of the South','of the East','of the West','of the City','of the Hills','of the Mountains','of the Plains','of the Woods','of the Coast','the Bold','the Daring','the Barbarian','the Civilized','the Battler','the Black','the Blue','the Brown','the Green','the Red','the Yellow','the Fearless','the Brave','the Fair','the Foul','the Lovely','the Loathsome','the Zeroeth','the First','the Second','the Third','the Fourth','the Fifth','the Sixth','the Seventh','the Eighth','the Nineth','the Tenth','the Eleventh','the Twelf','the Thirteenth','the Fourteen','the Fifteenth','the Sixteenth','the Seventeenth','the Eighteenth','the Nineteenth','the Twentieth','the Gentle','the Cruel','the Great','the Merciful','the Merciless','the Mighty','the Mysterious','the Unknown','the Old','the Young','the Boy','the Girl','the Quick','the Slow','the Quiet','the Silent','the Loud','the Steady','the Unready','the Traveller','the Wanderer','the Unexpected','the Hooded','the Cloaked','the Robed']
}
directions_pattern = '^[ABS]{1,3}$'