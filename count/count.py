from openerp import models,api,fields,exceptions
import logging

_logger = logging.getLogger(__name__)

EXPORTS_DIR = "./"
class count(models.Model):
	_name="count.count"

	name=fields.Char()

	@api.model
	def create(self,vals):
		self.count(8,6)
		return super(count,self).create(vals)

	def count(self,a,b):
		import pdb; pdb.set_trace()
		value='i am'
		fname=EXPORTS_DIR.join('test.txt')
		try:
			with open(fname,'w') as fobj:
				fobj.write('%s hereee ' % (value))
		except IOError:
			raise exceptions.UserError('unable to save file')
		return int(a+b)
