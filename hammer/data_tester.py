a = {
	'data': {
		'searchResults': {
			'fareSummary': [{
				'fareFamily': 'ANY',
				'minimumFare': {
					'value': '242.98',
					'currencyCode': 'USD'
				}
			}, {
				'fareFamily': 'WGA',
				'minimumFare': {
					'value': '149.98',
					'currencyCode': 'USD'
				}
			}, {
				'fareFamily': 'BUS',
				'minimumFare': {
					'value': '264.98',
					'currencyCode': 'USD'
				}
			}],
			'airProducts': [{
				'originationAirportCode': 'SLC',
				'destinationAirportCode': 'LAX',
				'containsAvailability': False,
				'containsNonstop': True,
				'containsBeforeNoon': True,
				'containsNoonToSix': True,
				'containsAfterSix': True,
				'containsTimeOfDay': True,
				'containsStops': True,
				'containsDirect': True,
				'currencyCode': None,
				'details': [{
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '17:10',
					'arrivalTime': '18:15',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4214',
						'legDuration': 125,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '17:10',
						'arrivalTime': '18:15',
						'departureDateTime': '2019-11-30T17:10:00.000-07:00',
						'arrivalDateTime': '2019-11-30T18:15:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 125,
					'flightNumbers': ['4214'],
					'filterTags': ['NOON_TO_SIX', 'NONSTOP', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T17:10:00.000-07:00',
					'arrivalDateTime': '2019-11-30T18:15:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,LAX,2019-11-30T17:10-07:00,2019-11-30T18:15-08:00,WN,WN,4214,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '30.25',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '242.98',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ZLNUWNR,Z,SLC,LAX,2019-11-30T17:10-07:00,2019-11-30T18:15-08:00,WN,WN,4214,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,LAX,2019-11-30T17:10-07:00,2019-11-30T18:15-08:00,WN,WN,4214,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '31.79',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '264.98',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '09:50',
					'arrivalTime': '12:40',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'PHX',
						'flightNumber': '4055',
						'legDuration': 100,
						'stopDuration': 40,
						'changePlanes': False,
						'departureTime': '09:50',
						'arrivalTime': '11:30',
						'departureDateTime': '2019-11-30T09:50:00.000-07:00',
						'arrivalDateTime': '2019-11-30T11:30:00.000-07:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'PHX',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4055',
						'legDuration': 90,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '12:10',
						'arrivalTime': '12:40',
						'departureDateTime': '2019-11-30T12:10:00.000-07:00',
						'arrivalDateTime': '2019-11-30T12:40:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 230,
					'flightNumbers': ['4055'],
					'filterTags': ['BEFORE_NOON', 'DIRECT', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T09:50:00.000-07:00',
					'arrivalDateTime': '2019-11-30T12:40:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,LAX,2019-11-30T09:50-07:00,2019-11-30T12:40-08:00,WN,WN,4055,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '34.45',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '247.18',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,LAX,2019-11-30T09:50-07:00,2019-11-30T12:40-08:00,WN,WN,4055,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,LAX,2019-11-30T09:50-07:00,2019-11-30T12:40-08:00,WN,WN,4055,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'seatsLeft': 2,
									'totalTaxesAndFees': {
										'value': '35.99',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '269.18',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '16:50',
					'arrivalTime': '19:15',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'LAS',
						'flightNumber': '4270',
						'legDuration': 75,
						'stopDuration': 55,
						'changePlanes': True,
						'departureTime': '16:50',
						'arrivalTime': '17:05',
						'departureDateTime': '2019-11-30T16:50:00.000-07:00',
						'arrivalDateTime': '2019-11-30T17:05:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'LAS',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4148',
						'legDuration': 75,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '18:00',
						'arrivalTime': '19:15',
						'departureDateTime': '2019-11-30T18:00:00.000-08:00',
						'arrivalDateTime': '2019-11-30T19:15:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 205,
					'flightNumbers': ['4270', '4148'],
					'filterTags': ['NOON_TO_SIX', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T16:50:00.000-07:00',
					'arrivalDateTime': '2019-11-30T19:15:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,LAS,2019-11-30T16:50-07:00,2019-11-30T17:05-08:00,WN,WN,4270,73W|YL,Y,LAS,LAX,2019-11-30T18:00-08:00,2019-11-30T19:15-08:00,WN,WN,4148,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,LAS,2019-11-30T16:50-07:00,2019-11-30T17:05-08:00,WN,WN,4270,73W|ALAUWNRO,A,LAS,LAX,2019-11-30T18:00-08:00,2019-11-30T19:15-08:00,WN,WN,4148,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,LAS,2019-11-30T16:50-07:00,2019-11-30T17:05-08:00,WN,WN,4270,73W|KZBP,K,LAS,LAX,2019-11-30T18:00-08:00,2019-11-30T19:15-08:00,WN,WN,4148,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '19:30',
					'arrivalTime': '23:05',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'LAS',
						'flightNumber': '3876',
						'legDuration': 80,
						'stopDuration': 125,
						'changePlanes': True,
						'departureTime': '19:30',
						'arrivalTime': '19:50',
						'departureDateTime': '2019-11-30T19:30:00.000-07:00',
						'arrivalDateTime': '2019-11-30T19:50:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'LAS',
						'destinationAirportCode': 'LAX',
						'flightNumber': '2469',
						'legDuration': 70,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '21:55',
						'arrivalTime': '23:05',
						'departureDateTime': '2019-11-30T21:55:00.000-08:00',
						'arrivalDateTime': '2019-11-30T23:05:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73H',
						'features': ['WIFI']
					}],
					'totalDuration': 275,
					'flightNumbers': ['3876', '2469'],
					'filterTags': ['AFTER_SIX', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T19:30:00.000-07:00',
					'arrivalDateTime': '2019-11-30T23:05:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,LAS,2019-11-30T19:30-07:00,2019-11-30T19:50-08:00,WN,WN,3876,73W|YL,Y,LAS,LAX,2019-11-30T21:55-08:00,2019-11-30T23:05-08:00,WN,WN,2469,73H',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,LAS,2019-11-30T19:30-07:00,2019-11-30T19:50-08:00,WN,WN,3876,73W|ALAUWNRO,A,LAS,LAX,2019-11-30T21:55-08:00,2019-11-30T23:05-08:00,WN,WN,2469,73H',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,LAS,2019-11-30T19:30-07:00,2019-11-30T19:50-08:00,WN,WN,3876,73W|KZBP,K,LAS,LAX,2019-11-30T21:55-08:00,2019-11-30T23:05-08:00,WN,WN,2469,73H',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '06:45',
					'arrivalTime': '10:45',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'PHX',
						'flightNumber': '3648',
						'legDuration': 100,
						'stopDuration': 100,
						'changePlanes': True,
						'departureTime': '06:45',
						'arrivalTime': '08:25',
						'departureDateTime': '2019-11-30T06:45:00.000-07:00',
						'arrivalDateTime': '2019-11-30T08:25:00.000-07:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'PHX',
						'destinationAirportCode': 'LAX',
						'flightNumber': '5684',
						'legDuration': 100,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '10:05',
						'arrivalTime': '10:45',
						'departureDateTime': '2019-11-30T10:05:00.000-07:00',
						'arrivalDateTime': '2019-11-30T10:45:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 300,
					'flightNumbers': ['3648', '5684'],
					'filterTags': ['BEFORE_NOON', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T06:45:00.000-07:00',
					'arrivalDateTime': '2019-11-30T10:45:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,PHX,2019-11-30T06:45-07:00,2019-11-30T08:25-07:00,WN,WN,3648,73W|YL,Y,PHX,LAX,2019-11-30T10:05-07:00,2019-11-30T10:45-08:00,WN,WN,5684,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,PHX,2019-11-30T06:45-07:00,2019-11-30T08:25-07:00,WN,WN,3648,73W|ALAUWNRO,A,PHX,LAX,2019-11-30T10:05-07:00,2019-11-30T10:45-08:00,WN,WN,5684,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,PHX,2019-11-30T06:45-07:00,2019-11-30T08:25-07:00,WN,WN,3648,73W|KZBP,K,PHX,LAX,2019-11-30T10:05-07:00,2019-11-30T10:45-08:00,WN,WN,5684,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '17:55',
					'arrivalTime': '22:05',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'PHX',
						'flightNumber': '2716',
						'legDuration': 95,
						'stopDuration': 130,
						'changePlanes': True,
						'departureTime': '17:55',
						'arrivalTime': '19:30',
						'departureDateTime': '2019-11-30T17:55:00.000-07:00',
						'arrivalDateTime': '2019-11-30T19:30:00.000-07:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'PHX',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4102',
						'legDuration': 85,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '21:40',
						'arrivalTime': '22:05',
						'departureDateTime': '2019-11-30T21:40:00.000-07:00',
						'arrivalDateTime': '2019-11-30T22:05:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 310,
					'flightNumbers': ['2716', '4102'],
					'filterTags': ['NOON_TO_SIX', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T17:55:00.000-07:00',
					'arrivalDateTime': '2019-11-30T22:05:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,PHX,2019-11-30T17:55-07:00,2019-11-30T19:30-07:00,WN,WN,2716,73W|YL,Y,PHX,LAX,2019-11-30T21:40-07:00,2019-11-30T22:05-08:00,WN,WN,4102,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,PHX,2019-11-30T17:55-07:00,2019-11-30T19:30-07:00,WN,WN,2716,73W|ALAUWNRO,A,PHX,LAX,2019-11-30T21:40-07:00,2019-11-30T22:05-08:00,WN,WN,4102,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,PHX,2019-11-30T17:55-07:00,2019-11-30T19:30-07:00,WN,WN,2716,73W|KZBP,K,PHX,LAX,2019-11-30T21:40-07:00,2019-11-30T22:05-08:00,WN,WN,4102,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '09:25',
					'arrivalTime': '13:40',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'SJC',
						'flightNumber': '2840',
						'legDuration': 120,
						'stopDuration': 110,
						'changePlanes': True,
						'departureTime': '09:25',
						'arrivalTime': '10:25',
						'departureDateTime': '2019-11-30T09:25:00.000-07:00',
						'arrivalDateTime': '2019-11-30T10:25:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '738',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'SJC',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4800',
						'legDuration': 85,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '12:15',
						'arrivalTime': '13:40',
						'departureDateTime': '2019-11-30T12:15:00.000-08:00',
						'arrivalDateTime': '2019-11-30T13:40:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73H',
						'features': ['WIFI']
					}],
					'totalDuration': 315,
					'flightNumbers': ['2840', '4800'],
					'filterTags': ['BEFORE_NOON', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T09:25:00.000-07:00',
					'arrivalDateTime': '2019-11-30T13:40:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,SJC,2019-11-30T09:25-07:00,2019-11-30T10:25-08:00,WN,WN,2840,738|YL,Y,SJC,LAX,2019-11-30T12:15-08:00,2019-11-30T13:40-08:00,WN,WN,4800,73H',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,SJC,2019-11-30T09:25-07:00,2019-11-30T10:25-08:00,WN,WN,2840,738|ALAUWNRO,A,SJC,LAX,2019-11-30T12:15-08:00,2019-11-30T13:40-08:00,WN,WN,4800,73H',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,SJC,2019-11-30T09:25-07:00,2019-11-30T10:25-08:00,WN,WN,2840,738|KZBP,K,SJC,LAX,2019-11-30T12:15-08:00,2019-11-30T13:40-08:00,WN,WN,4800,73H',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '11:15',
					'arrivalTime': '15:30',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'LAS',
						'flightNumber': '4520',
						'legDuration': 85,
						'stopDuration': 150,
						'changePlanes': True,
						'departureTime': '11:15',
						'arrivalTime': '11:40',
						'departureDateTime': '2019-11-30T11:15:00.000-07:00',
						'arrivalDateTime': '2019-11-30T11:40:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'LAS',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4992',
						'legDuration': 80,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '14:10',
						'arrivalTime': '15:30',
						'departureDateTime': '2019-11-30T14:10:00.000-08:00',
						'arrivalDateTime': '2019-11-30T15:30:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 315,
					'flightNumbers': ['4520', '4992'],
					'filterTags': ['BEFORE_NOON', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T11:15:00.000-07:00',
					'arrivalDateTime': '2019-11-30T15:30:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,LAS,2019-11-30T11:15-07:00,2019-11-30T11:40-08:00,WN,WN,4520,73W|YL,Y,LAS,LAX,2019-11-30T14:10-08:00,2019-11-30T15:30-08:00,WN,WN,4992,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,LAS,2019-11-30T11:15-07:00,2019-11-30T11:40-08:00,WN,WN,4520,73W|ALAUWNRO,A,LAS,LAX,2019-11-30T14:10-08:00,2019-11-30T15:30-08:00,WN,WN,4992,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,LAS,2019-11-30T11:15-07:00,2019-11-30T11:40-08:00,WN,WN,4520,73W|KZBP,K,LAS,LAX,2019-11-30T14:10-08:00,2019-11-30T15:30-08:00,WN,WN,4992,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '06:30',
					'arrivalTime': '11:15',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'DEN',
						'flightNumber': '4684',
						'legDuration': 95,
						'stopDuration': 100,
						'changePlanes': True,
						'departureTime': '06:30',
						'arrivalTime': '08:05',
						'departureDateTime': '2019-11-30T06:30:00.000-07:00',
						'arrivalDateTime': '2019-11-30T08:05:00.000-07:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73H',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'DEN',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4078',
						'legDuration': 150,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '09:45',
						'arrivalTime': '11:15',
						'departureDateTime': '2019-11-30T09:45:00.000-07:00',
						'arrivalDateTime': '2019-11-30T11:15:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 345,
					'flightNumbers': ['4684', '4078'],
					'filterTags': ['BEFORE_NOON', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T06:30:00.000-07:00',
					'arrivalDateTime': '2019-11-30T11:15:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,DEN,2019-11-30T06:30-07:00,2019-11-30T08:05-07:00,WN,WN,4684,73H|YL,Y,DEN,LAX,2019-11-30T09:45-07:00,2019-11-30T11:15-08:00,WN,WN,4078,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,DEN,2019-11-30T06:30-07:00,2019-11-30T08:05-07:00,WN,WN,4684,73H|ALAUWNRO,A,DEN,LAX,2019-11-30T09:45-07:00,2019-11-30T11:15-08:00,WN,WN,4078,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,DEN,2019-11-30T06:30-07:00,2019-11-30T08:05-07:00,WN,WN,4684,73H|KZBP,K,DEN,LAX,2019-11-30T09:45-07:00,2019-11-30T11:15-08:00,WN,WN,4078,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '12:20',
					'arrivalTime': '17:05',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'SMF',
						'flightNumber': '5711',
						'legDuration': 105,
						'stopDuration': 155,
						'changePlanes': True,
						'departureTime': '12:20',
						'arrivalTime': '13:05',
						'departureDateTime': '2019-11-30T12:20:00.000-07:00',
						'arrivalDateTime': '2019-11-30T13:05:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'SMF',
						'destinationAirportCode': 'LAX',
						'flightNumber': '1872',
						'legDuration': 85,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '15:40',
						'arrivalTime': '17:05',
						'departureDateTime': '2019-11-30T15:40:00.000-08:00',
						'arrivalDateTime': '2019-11-30T17:05:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 345,
					'flightNumbers': ['5711', '1872'],
					'filterTags': ['NOON_TO_SIX', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T12:20:00.000-07:00',
					'arrivalDateTime': '2019-11-30T17:05:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,SMF,2019-11-30T12:20-07:00,2019-11-30T13:05-08:00,WN,WN,5711,73W|YL,Y,SMF,LAX,2019-11-30T15:40-08:00,2019-11-30T17:05-08:00,WN,WN,1872,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,SMF,2019-11-30T12:20-07:00,2019-11-30T13:05-08:00,WN,WN,5711,73W|ALAUWNRO,A,SMF,LAX,2019-11-30T15:40-08:00,2019-11-30T17:05-08:00,WN,WN,1872,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,SMF,2019-11-30T12:20-07:00,2019-11-30T13:05-08:00,WN,WN,5711,73W|KZBP,K,SMF,LAX,2019-11-30T15:40-08:00,2019-11-30T17:05-08:00,WN,WN,1872,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '15:40',
					'arrivalTime': '20:35',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'DEN',
						'flightNumber': '3849',
						'legDuration': 80,
						'stopDuration': 125,
						'changePlanes': True,
						'departureTime': '15:40',
						'arrivalTime': '17:00',
						'departureDateTime': '2019-11-30T15:40:00.000-07:00',
						'arrivalDateTime': '2019-11-30T17:00:00.000-07:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'DEN',
						'destinationAirportCode': 'LAX',
						'flightNumber': '5753',
						'legDuration': 150,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '19:05',
						'arrivalTime': '20:35',
						'departureDateTime': '2019-11-30T19:05:00.000-07:00',
						'arrivalDateTime': '2019-11-30T20:35:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 355,
					'flightNumbers': ['3849', '5753'],
					'filterTags': ['NOON_TO_SIX', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T15:40:00.000-07:00',
					'arrivalDateTime': '2019-11-30T20:35:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,DEN,2019-11-30T15:40-07:00,2019-11-30T17:00-07:00,WN,WN,3849,73W|YL,Y,DEN,LAX,2019-11-30T19:05-07:00,2019-11-30T20:35-08:00,WN,WN,5753,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'seatsLeft': 2,
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,DEN,2019-11-30T15:40-07:00,2019-11-30T17:00-07:00,WN,WN,3849,73W|ALAUWNRO,A,DEN,LAX,2019-11-30T19:05-07:00,2019-11-30T20:35-08:00,WN,WN,5753,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,DEN,2019-11-30T15:40-07:00,2019-11-30T17:00-07:00,WN,WN,3849,73W|KZBP,K,DEN,LAX,2019-11-30T19:05-07:00,2019-11-30T20:35-08:00,WN,WN,5753,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'seatsLeft': 2,
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '17:55',
					'arrivalTime': '23:10',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'PHX',
						'flightNumber': '2716',
						'legDuration': 95,
						'stopDuration': 190,
						'changePlanes': True,
						'departureTime': '17:55',
						'arrivalTime': '19:30',
						'departureDateTime': '2019-11-30T17:55:00.000-07:00',
						'arrivalDateTime': '2019-11-30T19:30:00.000-07:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}, {
						'originationAirportCode': 'PHX',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4347',
						'legDuration': 90,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '22:40',
						'arrivalTime': '23:10',
						'departureDateTime': '2019-11-30T22:40:00.000-07:00',
						'arrivalDateTime': '2019-11-30T23:10:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 375,
					'flightNumbers': ['2716', '4347'],
					'filterTags': ['NOON_TO_SIX', 'STOPS', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T17:55:00.000-07:00',
					'arrivalDateTime': '2019-11-30T23:10:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,PHX,2019-11-30T17:55-07:00,2019-11-30T19:30-07:00,WN,WN,2716,73W|YL,Y,PHX,LAX,2019-11-30T22:40-07:00,2019-11-30T23:10-08:00,WN,WN,4347,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '38.95',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '251.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|ALAUWNRO,A,SLC,PHX,2019-11-30T17:55-07:00,2019-11-30T19:30-07:00,WN,WN,2716,73W|ALAUWNRO,A,PHX,LAX,2019-11-30T22:40-07:00,2019-11-30T23:10-08:00,WN,WN,4347,73W',
								'classOfService': None,
								'passengerType': 'ADULT',
								'availabilityStatus': 'SOLD_OUT',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,PHX,2019-11-30T17:55-07:00,2019-11-30T19:30-07:00,WN,WN,2716,73W|KZBP,K,PHX,LAX,2019-11-30T22:40-07:00,2019-11-30T23:10-08:00,WN,WN,4347,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '40.49',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '273.68',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}, {
					'originationAirportCode': 'SLC',
					'destinationAirportCode': 'LAX',
					'departureTime': '07:40',
					'arrivalTime': '08:50',
					'nextDay': False,
					'stopsDetails': [{
						'originationAirportCode': 'SLC',
						'destinationAirportCode': 'LAX',
						'flightNumber': '4206',
						'legDuration': 130,
						'stopDuration': 0,
						'changePlanes': None,
						'departureTime': '07:40',
						'arrivalTime': '08:50',
						'departureDateTime': '2019-11-30T07:40:00.000-07:00',
						'arrivalDateTime': '2019-11-30T08:50:00.000-08:00',
						'operatingCarrierCode': 'WN',
						'marketingCarrierCode': 'WN',
						'aircraftEquipmentType': '73W',
						'features': ['WIFI']
					}],
					'totalDuration': 130,
					'flightNumbers': ['4206'],
					'filterTags': ['BEFORE_NOON', 'NONSTOP', 'AVAILABLE'],
					'departureDateTime': '2019-11-30T07:40:00.000-07:00',
					'arrivalDateTime': '2019-11-30T08:50:00.000-08:00',
					'fareProducts': {
						'ADULT': {
							'ANY': {
								'productId': 'ANY|ADT|YL,Y,SLC,LAX,2019-11-30T07:40-07:00,2019-11-30T08:50-08:00,WN,WN,4206,73W',
								'classOfService': 'Y',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '212.73',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '30.25',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '242.98',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2128'
								},
								'waivedFare': None
							},
							'WGA': {
								'productId': 'WGA|ADT|CLNUPNR,C,SLC,LAX,2019-11-30T07:40-07:00,2019-11-30T08:50-08:00,WN,WN,4206,73W',
								'classOfService': 'C',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '126.21',
										'currencyCode': 'USD'
									},
									'seatsLeft': 2,
									'totalTaxesAndFees': {
										'value': '23.77',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '149.98',
										'currencyCode': 'USD'
									},
									'accrualPoints': '758'
								},
								'waivedFare': None
							},
							'BUS': {
								'productId': 'BUS|ADT|KZBP,K,SLC,LAX,2019-11-30T07:40-07:00,2019-11-30T08:50-08:00,WN,WN,4206,73W',
								'classOfService': 'K',
								'passengerType': 'ADULT',
								'availabilityStatus': 'AVAILABLE',
								'originalFare': None,
								'fare': {
									'baseFare': {
										'value': '233.19',
										'currencyCode': 'USD'
									},
									'totalTaxesAndFees': {
										'value': '31.79',
										'currencyCode': 'USD'
									},
									'totalFare': {
										'value': '264.98',
										'currencyCode': 'USD'
									},
									'accrualPoints': '2799'
								},
								'waivedFare': None
							}
						},
						'SENIOR': {
							'ANY': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'WGA': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							},
							'BUS': {
								'productId': None,
								'classOfService': None,
								'passengerType': None,
								'availabilityStatus': 'UNAVAILABLE',
								'originalFare': None,
								'fare': {},
								'waivedFare': None
							}
						}
					}
				}],
				'lowestFare': {
					'fareFamily': 'WGA',
					'currencyCode': 'USD',
					'value': '149.98'
				}
			}],
			'promoToken': None
		}
	},
	'success': True,
	'notifications': None,
	'uiMetadata': {
		'paymentInfoService': True,
		'discountServiceMaintenanceModeForDotcom': False,
		'discountServiceMaintenanceModeForSwabiz': False,
		'cvvForSavedCreditCard': True,
		'cvvForSavedCreditCardSwabiz': True,
		'carCrossSellEnabled': True,
		'cvvForEnteredCreditCardSwabiz': False,
		'chapiVersion': '1.23.2',
		'lowFareCalendarService': True,
		'airFirstTimeFlyer': True,
		'rapidRewardsMaintenance': False,
		'earlyBirdCrossSellEnabled': True,
		'proxyLogout': True,
		'payPalService': True,
		'fundsService': True
	}
}
