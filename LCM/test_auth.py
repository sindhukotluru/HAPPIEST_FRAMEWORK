import auth

status1 = auth.local_user_authentication_test_without_admin_privilage('10.16.84.236', 'vyos', 'vyos', 'test', 'test123', None, 'local')


status2 = auth.local_user_authentication_test_with_admin_privilage('10.16.84.236', 'vyos', 'vyos', 'test', 'test123', 'admin', 'local')


status3 = auth.radius_user_authentication_test('10.16.84.236', 'vyos', 'vyos',  '10.16.84.238', 'testuser', 'raduser', 'radpass', '1812', '30', 'RADIUS')

