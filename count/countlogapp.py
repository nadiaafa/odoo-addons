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
		value='i am'
		_logger.debug('%d here we are', int(a+b))
		fname=EXPORTS_DIR.join('test.txt')
		try:
			with open(fname,'w') as fobj:
				fobj.write('%s hereee ' % (value))
		except IOError:
			_logger.exception('error writing to %s in %s','test.txt',EXPORTS_DIR)
			raise exceptions.UserError('unable to save file')
		return int(a+b)
