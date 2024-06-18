bbt_s12 = [{'title': 'The Conjugal Configuration', 'duration': 20},
           {'title': 'The Wedding Gift Wormhole', 'duration': 21},
           {'title': 'The Procreation Calculation', 'duration': 20},
           {'title': 'The Tam Turbulence', 'duration': 19},
           {'title': 'The Planetarium Collision', 'duration': 19},
           {'title': 'The Imitation Perturbation', 'duration': 19},
           {'title': 'The Grant Allocation Derivation', 'duration': 19},
           {'title': 'The Consummation Deviation', 'duration': 22},
           {'title': 'The Citation Negation', 'duration': 20},
           {'title': 'The VCR Illumination', 'duration': 20},
           {'title': 'The Paintball Scattering', 'duration': 19},
           {'title': 'The Propagation Proposition', 'duration': 20},
           {'title': 'The Confirmation Polarization', 'duration': 20},
           {'title': 'The Meteorite Manifestation', 'duration': 19},
           {'title': 'The Donation Oscillation', 'duration': 21},
           {'title': 'The D & D Vortex', 'duration': 20},
           {'title': 'The Conference Valuation', 'duration': 19},
           {'title': 'The Laureate Accumulation', 'duration': 21},
           {'title': 'The Inspiration Deprivation', 'duration': 20},
           {'title': 'The Decision Reverberation', 'duration': 19},
           {'title': 'The Plagiarism Schism', 'duration': 19},
           {'title': 'The Maternal Conclusion', 'duration': 20},
           {'title': 'The Change Constant', 'duration': 19},
           {'title': 'The Stockholm Syndrome', 'duration': 23}]

EPISODE_DURATION = 23

print(len(bbt_s12) * EPISODE_DURATION)

time_remaining = 120

print(time_remaining // EPISODE_DURATION)

print(bbt_s12[:time_remaining // EPISODE_DURATION])
