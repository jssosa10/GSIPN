import time
import numpy as np
import pandas as pd

class GSIPN(object):
	"""docstring for GSIPN"""
	def __init__(self):
		self.places = {}
		self.transitions = {}
		self.inArcs = {}
		self.outArcs = {}
		self.global_varibles = {}

	def  add_place(self, name, tokens=0):
		self.places[name] = tokens

	def add_transition(self, name, t_class='im', rate=None, predicate = None, assertion = None):
		self.transitions[name]={'class': t_class,'rate': rate, 'predicate': predicate, 'assertion': assertion}

	def add_tokens(self, place_name, ntokens):
		self.places[place_name] = self.places[place_name]+ntokens

	def remove_token(self, place_name, ntokens):
		self.places[place_name] = self.places[place_name]-ntokens

	def add_varible(self, name, value):
		self.global_varibles[name] = value

	def get_current_markings(self):
		return self.places.copy()

	def add_inArc(self, place, transition, weight=1):
		if transition in self.inArcs:
			self.inArcs[transition] = self.inArcs[transition].append({'place':place,'weight':weight})
		else:
			self.inArcs[transition] = [{'place':place,'weight':weight}]

	def add_outArc(self, place, transition, weight=1):
		if transition in self.outArcs:
			self.outArcs[transition] = self.outArcs[transition].append({'place':place,'weight':weight})
		else:
			self.outArcs[transition] = [{'place':place,'weight':weight}]			

	def add_variable(self, key, val):
		self.global_varibles[key]=val

	def get_enabled_transitions(self):
		enabled_exp_transitions = []
		enabled_transitions = []
		for transition in self.transitions:
			can = True
			tname = transition
			transition = self.transitions[transition]
			##print transition
			arcs = self.inArcs[tname]
			for arc in arcs:
				can = can and self.places[arc['place']]>=arc['weight']

			if transition['predicate']:
				can = can and eval(transition['predicate'],self.global_varibles)

			if can:
				if transition['class'] == 'im':
					enabled_transitions.append(tname)

				else:
					enabled_exp_transitions.append(tname)

		return enabled_exp_transitions, enabled_transitions

	def fire_transition(self, transition):
		arcs = self.inArcs[transition]
		for arc in arcs:
			self.places[arc['place']] = self.places[arc['place']]-arc['weight']

		arcs  = self.outArcs[transition]
		for arc in arcs:
			self.places[arc['place']] = self.places[arc['place']]+arc['weight']

		if self.transitions[transition]['assertion']:
			exec(self.transitions[transition]['assertion'],self.global_varibles)
		##print self.places


	def simulate(self, steps, report=1, simulate_wait=False):
		markings = []
		for step in range(steps):
			if step % report == 0:
				markings.append(self.get_current_markings())

			enabled_exp_transitions, enabled_transitions = self.get_enabled_transitions()

			if enabled_transitions:
				if len(enabled_transitions) > 1:
					firing_transition = np.random.choice(a=enabled_transitions, size=None)
					self.fire_transition(firing_transition)
				else:
					self.fire_transition(enabled_transitions[0])
			elif enabled_exp_transitions:
				if len(enabled_exp_transitions) > 1:
					s = 0
					possible_transitions = []
					probabilities = []
					for transition in enabled_exp_transitions:
						s+=self.transitions[transition]['rate']
					for transition in enabled_exp_transitions:
						probabilities.append(self.transitions[transition]['rate']/s)
						possible_transitions.append(transition)
					##print '////////////////////'
					##print probabilities
					##print possible_transitions
					firing_transition = np.random.choice(a=possible_transitions,size=None,p=probabilities)
					##print firing_transition
					
					self.fire_transition(firing_transition)
					##print '///////////////////'

				else:
					self.fire_transition(enabled_exp_transitions[0])
		return markings







