from utils.config_reader import read
from utils.config_operations import *

config = read('Test','golem')
build_full_config(config)

# config = {
#     'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
#     'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
#     'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
#     'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
#     'local_music_location': '/usr/data/music'
# }
# import music

# pandora = music.factory.create('PANDORA', **config)
# pandora.test_connection()

# spotify = music.factory.create('SPOTIFY', **config)
# spotify.test_connection()

# local = music.factory.create('LOCAL', **config)
# local.test_connection()

# pandora2 = music.services.get('PANDORA', **config)
# print(f'id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}')

# spotify2 = music.services.get('SPOTIFY', **config)
# print(f'id(spotify) == id(spotify2): {id(spotify) == id(spotify2)}')

# import music

# config = {
#     'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
#     'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
#     'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
#     'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
#     'local_music_location': '/usr/data/music'
# }

# pandora = music.services.get('PANDORA', **config)
# pandora.test_connection()
# spotify = music.services.get('SPOTIFY', **config)
# spotify.test_connection()
# local = music.services.get('LOCAL', **config)
# local.test_connection()

# pandora2 = music.services.get('PANDORA', **config)
# print(f'id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}')

# spotify2 = music.services.get('SPOTIFY', **config)
# print(f'id(spotify) == id(spotify2): {id(spotify) == id(spotify2)}')

"""
[loop_i],Energy
[loop_i-cycle_relay],Energy
[loop_i-noise_ctrl],Energy
[loop_i-cntxt_relay],Energy
[Gate_i],Energy
noise_ctrl:noise_dwn_inhib,noise_adj_inhib
cycle_relay:cycle_gate_ctrl,cycle_stg_adv
cntxt_relay:cntxt_stg_adv,cntxt_up_inhib
relay:stg_adv

loop_i-noise_ctrl:loop_i
loop_i-cycle_relay:loop_i
loop_i-cntxt_relay:loop_i
Gate_i-relay:Gate_i

*: [loop_i,Energy]
noise_dwn_inhib: [loop_i-noise_dwn_inhibPrev,Bool,noise_adj_inhib,Energy,loop_i-noise_ctrl,Energy]
noise_adj_inhib: [loop_i-noise_adj_inhibPrev,Bool,loop_i-noise_ctrl,Energy]
cycle_gate_ctrl: [loop_i-cycle_stg_advPrev,Bool,loop_i-cycle_relay,Energy]
cycle_stg_adv: [loop_i-cycle_stg_advPrev,Bool,loop_i-cycle_relay,Energy]
cntxt_stg_adv: [loop_i-cntxt_stg_advPrev,Bool,loop_i-cntxt_relay,Energy]
cntxt_up_inhib: [loop_i-cntxt_up_inhibPrev,Bool,loop_i-cntxt_relay,Energy]
relay: [Gate_i,Energy, Gate_i-Prev,Bool]

noise_dwn_inhib: [Plate,1],1
noise_adj_inhib: [Plate,1],1
cycle_gate_ctrl: [Point,1],1
cycle_stg_adv: [Point,1],1
cntxt_stg_adv: [Plate,1],1
cntxt_up_inhib: [Plate,1],1
relay:[Point,1],1

noise_dwn_inhib: [loop_i-cntxt_up_inhib,Inhbitor,G-cycle_relay,Inhibitor,G-cntxt_relay,Inhibitor]
noise_adj_inhib: [loop_i-noise_dwn_inhib,Inhibitor]
cycle_gate_ctrl: [loop_i-cycle_relay,Inhibitor]
cycle_stg_adv: [loop_i-cycle_relay,Energy,loop_i-cntxt_ctrl,Energy,loop_i-proc_ctrl,Energy]
cntxt_stg_adv: [loop_i-cntxt_relay,Energy,loop_i-cntxt_ctrl,Energy,loop_i-proc_ctrl,Energy]
cntxt_up_inhib: [loop_i-cntxt_relay,Inhibitor]
relay:[Gate_i-]

loop_i-proc_ctrl,Energy
loop_i-cntxt_ctrl,Energy
loop_i-noise_ctrl,Energy
OutputCtrl-loop_i,Energy

If every link has subdest keys, then we can define them separately from the InputMelds,&ProcGroupInputMelds
ProcGroups produce ouput however. If links only use the processed versions of the module output, we can ignore defining proc group to proc group specific mappings
ShapeComposition is the key here
loop_i
loop_i,Energy
loop_i-cycle_relay
loop_i-cycle_relay,Energy
loop_i-noise_ctrl
loop_i-noise_ctrl,Energy
loop_i-cntxt_relay
loop_i-cntxt_relay,Energy
loop_i-noise_dwn_inhibPrev,Bool
loop_i-noise_adj_inhib,Energy
loop_i-noise_adj_inhibPrev,Bool
loop_i-cycle_stg_advPrev,Bool
loop_i-cntxt_stg_advPrev,Bool
loop_i-cntxt_up_inhibPrev,Bool
loop_i-cntxt_up_inhib,Inhbitor
G-cycle_relay,Inhibitor
G-cntxt_relay,Inhibitor
loop_i-noise_dwn_inhib,Inhibitor
loop_i-cycle_relay,Inhibitor
loop_i-cntxt_relay,Inhibitor
loop_i-proc_ctrl,Energy
loop_i-cntxt_ctrl,Energy
B1,Energy
TestInput,Energy,TestInputWhl
G_TestA-proc_ctrl,Energy,TestInputWhl
G_TestA-cntxt_ctrl,Energy,TestInputWhl
"""