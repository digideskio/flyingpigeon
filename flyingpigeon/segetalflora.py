def get_equation(culture_type= 'fallow', climate_type=2):
  """
  example: 
  eq = get_equation(culture_type= 'fallow', climate_type=2)
  """
  climate_type = str(climate_type)
  if culture_type == 'fallow':  
    if climate_type == '1': 
      equation = "\'sf_fallow_1=exp(46.4619-15.4355*(%s-273.15)+0.7070*((%s-273.15)^2))\'" %('tas','tas')
    elif climate_type == '2': 
      equation = "\'sf_fallow_2=66.463*exp(-0.1315*(%s-273.15))\'"  %('tas')
    elif climate_type == '3': 
      equation ="\'sf_fallow_3=exp(1.837+0.2856*(%s-273.15)-0.0156*(%s-273.15)^2)\'" %('tas','tas')
    elif climate_type == '4': 
      equation ="\'sf_fallow_4=0.0685*(%s-273.15)^3-2.9184*(%s-273.15)^2+38.864*(%s-273.15)-80.046\'" %('tas','tas','tas')
    elif climate_type == '5': 
      equation ="\'sf_fallow_5=1.68*exp(0.735*exp(0.1134*(%s-273.15)))\'" %('tas')
    elif climate_type == '6': 
      equation ="\'sf_fallow_6=0.0088*(%s-273.15)^3-0.3457*(%s-273.15)^2+3.6656*(%s-273.15)+5.3486\'" %('tas','tas','tas')
    elif climate_type == '7': 
      equation ="\'sf_fallow_7=3.4655*exp(0.1303*(%s-273.15))\'" %('tas')
    elif climate_type == 'all': 
      equation ="\'sf_fallow_a=0.2787*(%s-273.15)^3-7.5658*(%s-273.15)^2+72.4143*(%s-273.15)-76.29\'" %('tas','tas','tas')
    else: 
      equation = 'no equation found'
        
  elif culture_type == 'extensiv': 
    if climate_type == '1': 
      equation ="\'sf_extensiv_1=exp(46.0518-15.4597*%s+0.7143*%s^2)\'" %('tas','tas')
    elif climate_type == '2': 
      equation ="\'sf_extensiv_2=45.6589*exp(-0.0987*%s)\'"%('tas')
    elif climate_type == '3': 
      equation ="\'sf_extensiv_3=exp(1.4383+0.33*%s-0.0176*%s^2)\'"%('tas','tas')
    elif climate_type == '4': 
      equation ="\'sf_extensiv_4=-0.7587*%s^2+17.8515*%s-32.8794\'"%('tas','tas')
    elif climate_type == '5': 
      equation ="\'sf_extensiv_5=0.0817*exp(0.4597*%s)\'"%('tas')
    elif climate_type == '6': 
      equation ="\'sf_extensiv_6=-0.0263*%s^3+0.7119*%s^2-4.878*%s+11.154\'" %('tas','tas','tas')
    elif climate_type == '7': 
      equation ="\'sf_extensiv_7=1.1653*exp(0.1711*%s)\'"%('tas')
    elif climate_type == 'all': 
      equation ="\'sf_extensiv_all=0.2386*%s^3-6.5351*%s^2+62.475*%s-73.9023\'" %('tas','tas','tas')
    else: 
      equation = None
  
  elif culture_type == 'intensiv': 
    if climate_type == '1': 
      equation ="\'sf_intensiv_1=exp(46,0518-15,4597*%s+0,7143*%s^2)\'" %('tas','tas')
    elif climate_type == '2': 
      equation ="\'sf_intensiv_2=31,3493*exp(-0,1108*%s)\'" %('tas')
    elif climate_type == '3': 
      equation ="\'sf_intensiv_3=exp(1,0791+0,3449*%s-0,0189*%s^2)\'" %('tas','tas')
    elif climate_type == '4': 
      equation ="\'sf_intensiv_4=-0,0919**%s^3+2,3824*%s^2-14,29*%s+38,93\'" %('tas','tas','tas')
    elif climate_type == '5': 
      equation ="\'sf_intensiv_5=exp(0,1663+0,0457*%s+0,0128*%s^2)\'" %('tas','tas')
    elif climate_type == '6': 
      equation ="\'sf_intensiv_6=14,1641*exp(-0,0363*%s)\'" %('tas')
    elif climate_type == '7': 
      equation ="\'sf_intensiv_7=1,704*exp(0,0982*%s)\'" %('tas')
    elif climate_type == 'all': 
      equation ="\'sf_intensiv_all=43,2846*exp(0,071*%s)\'" %('tas')
    else: 
      equation = None    
  else: 
    equation = None
     
  return equation  

      