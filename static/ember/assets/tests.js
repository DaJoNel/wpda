'use strict';

define('wpda-client/tests/acceptance/places-test', ['exports', 'ember', 'qunit', 'wpda-client/tests/helpers/start-app'], function (exports, _ember, _qunit, _wpdaClientTestsHelpersStartApp) {

  var application;
  var originalConfirm;
  var confirmCalledWith;

  (0, _qunit.module)('Acceptance: Place', {
    beforeEach: function beforeEach() {
      application = (0, _wpdaClientTestsHelpersStartApp['default'])();
      originalConfirm = window.confirm;
      window.confirm = function () {
        confirmCalledWith = [].slice.call(arguments);
        return true;
      };
    },
    afterEach: function afterEach() {
      _ember['default'].run(application, 'destroy');
      window.confirm = originalConfirm;
      confirmCalledWith = null;
    }
  });

  (0, _qunit.test)('visiting /places without data', function (assert) {
    visit('/places');

    andThen(function () {
      assert.equal(currentPath(), 'places.index');
      assert.equal(find('#blankslate').text().trim(), 'No Places found');
    });
  });

  (0, _qunit.test)('visiting /places with data', function (assert) {
    server.create('place');
    visit('/places');

    andThen(function () {
      assert.equal(currentPath(), 'places.index');
      assert.equal(find('#blankslate').length, 0);
      assert.equal(find('table tbody tr').length, 1);
    });
  });

  (0, _qunit.test)('create a new place', function (assert) {
    visit('/places');
    click('a:contains(New Place)');

    andThen(function () {
      assert.equal(currentPath(), 'places.new');

      fillIn('label:contains(Is verified) input', 'MyString');
      fillIn('label:contains(Venue) input', 'MyString');
      fillIn('label:contains(Name) input', 'MyString');
      fillIn('label:contains(Permalink) input', 'MyString');
      fillIn('label:contains(Lock level) input', 'MyString');
      fillIn('label:contains(Categories) input', 'MyString');
      fillIn('label:contains(Number) input', 'MyString');
      fillIn('label:contains(Street) input', 'MyString');
      fillIn('label:contains(City) input', 'MyString');
      fillIn('label:contains(State) input', 'MyString');
      fillIn('label:contains(Country) input', 'MyString');
      fillIn('label:contains(Updated by) input', 'MyString');
      fillIn('label:contains(Updated on) input', 'MyString');
      fillIn('label:contains(User report on) input', 'MyString');
      fillIn('label:contains(Is residential) input', false);

      click('input:submit');
    });

    andThen(function () {
      assert.equal(find('#blankslate').length, 0);
      assert.equal(find('table tbody tr').length, 1);
    });
  });

  (0, _qunit.test)('update an existing place', function (assert) {
    server.create('place');
    visit('/places');
    click('a:contains(Edit)');

    andThen(function () {
      assert.equal(currentPath(), 'places.edit');

      fillIn('label:contains(Is verified) input', 'MyString');
      fillIn('label:contains(Venue) input', 'MyString');
      fillIn('label:contains(Name) input', 'MyString');
      fillIn('label:contains(Permalink) input', 'MyString');
      fillIn('label:contains(Lock level) input', 'MyString');
      fillIn('label:contains(Categories) input', 'MyString');
      fillIn('label:contains(Number) input', 'MyString');
      fillIn('label:contains(Street) input', 'MyString');
      fillIn('label:contains(City) input', 'MyString');
      fillIn('label:contains(State) input', 'MyString');
      fillIn('label:contains(Country) input', 'MyString');
      fillIn('label:contains(Updated by) input', 'MyString');
      fillIn('label:contains(Updated on) input', 'MyString');
      fillIn('label:contains(User report on) input', 'MyString');
      fillIn('label:contains(Is residential) input', false);

      click('input:submit');
    });

    andThen(function () {
      assert.equal(find('#blankslate').length, 0);
      assert.equal(find('table tbody tr').length, 1);
    });
  });

  (0, _qunit.test)('show an existing place', function (assert) {
    server.create('place');
    visit('/places');
    click('a:contains(Show)');

    andThen(function () {
      assert.equal(currentPath(), 'places.show');

      assert.equal(find('p strong:contains(Is verified:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Venue:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Name:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Permalink:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Lock level:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Categories:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Number:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Street:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(City:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(State:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Country:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Updated by:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Updated on:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(User report on:)').next().text(), 'MyString');
      assert.equal(find('p strong:contains(Is residential:)').next().text(), false);
    });
  });

  (0, _qunit.test)('delete a place', function (assert) {
    server.create('place');
    visit('/places');
    click('a:contains(Remove)');

    andThen(function () {
      assert.equal(currentPath(), 'places.index');
      assert.deepEqual(confirmCalledWith, ['Are you sure?']);
      assert.equal(find('#blankslate').length, 1);
    });
  });
});
define('wpda-client/tests/acceptance/places-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | acceptance/places-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(false, 'acceptance/places-test.js should pass jshint.\nacceptance/places-test.js: line 35, col 3, \'server\' is not defined.\nacceptance/places-test.js: line 78, col 3, \'server\' is not defined.\nacceptance/places-test.js: line 111, col 3, \'server\' is not defined.\nacceptance/places-test.js: line 137, col 3, \'server\' is not defined.\n\n4 errors');
  });
});
define('wpda-client/tests/adapters/application.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | adapters/application.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/application.js should pass jshint.');
  });
});
define('wpda-client/tests/app.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | app.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'app.js should pass jshint.');
  });
});
define('wpda-client/tests/authenticators/drf-token-authenticator.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | authenticators/drf-token-authenticator.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(false, 'authenticators/drf-token-authenticator.js should pass jshint.\nauthenticators/drf-token-authenticator.js: line 33, col 30, \'error\' is defined but never used.\nauthenticators/drf-token-authenticator.js: line 33, col 22, \'status\' is defined but never used.\n\n2 errors');
  });
});
define('wpda-client/tests/authorizers/drf-token-authorizer.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | authorizers/drf-token-authorizer.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'authorizers/drf-token-authorizer.js should pass jshint.');
  });
});
define('wpda-client/tests/controllers/application.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | controllers/application.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/application.js should pass jshint.');
  });
});
define('wpda-client/tests/controllers/login.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | controllers/login.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/login.js should pass jshint.');
  });
});
define('wpda-client/tests/controllers/register.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | controllers/register.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(false, 'controllers/register.js should pass jshint.\ncontrollers/register.js: line 25, col 22, \'response\' is defined but never used.\ncontrollers/register.js: line 27, col 30, \'error\' is defined but never used.\ncontrollers/register.js: line 27, col 22, \'status\' is defined but never used.\n\n3 errors');
  });
});
define('wpda-client/tests/helpers/destroy-app', ['exports', 'ember'], function (exports, _ember) {
  exports['default'] = destroyApp;

  function destroyApp(application) {
    _ember['default'].run(application, 'destroy');
  }
});
define('wpda-client/tests/helpers/destroy-app.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | helpers/destroy-app.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/destroy-app.js should pass jshint.');
  });
});
define('wpda-client/tests/helpers/ember-simple-auth', ['exports', 'ember-simple-auth/authenticators/test'], function (exports, _emberSimpleAuthAuthenticatorsTest) {
  exports.authenticateSession = authenticateSession;
  exports.currentSession = currentSession;
  exports.invalidateSession = invalidateSession;

  var TEST_CONTAINER_KEY = 'authenticator:test';

  function ensureAuthenticator(app, container) {
    var authenticator = container.lookup(TEST_CONTAINER_KEY);
    if (!authenticator) {
      app.register(TEST_CONTAINER_KEY, _emberSimpleAuthAuthenticatorsTest['default']);
    }
  }

  function authenticateSession(app, sessionData) {
    var container = app.__container__;

    var session = container.lookup('service:session');
    ensureAuthenticator(app, container);
    session.authenticate(TEST_CONTAINER_KEY, sessionData);
    return wait();
  }

  ;

  function currentSession(app) {
    return app.__container__.lookup('service:session');
  }

  ;

  function invalidateSession(app) {
    var session = app.__container__.lookup('service:session');
    if (session.get('isAuthenticated')) {
      session.invalidate();
    }
    return wait();
  }

  ;
});
define('wpda-client/tests/helpers/module-for-acceptance', ['exports', 'qunit', 'ember', 'wpda-client/tests/helpers/start-app', 'wpda-client/tests/helpers/destroy-app'], function (exports, _qunit, _ember, _wpdaClientTestsHelpersStartApp, _wpdaClientTestsHelpersDestroyApp) {
  var Promise = _ember['default'].RSVP.Promise;

  exports['default'] = function (name) {
    var options = arguments.length <= 1 || arguments[1] === undefined ? {} : arguments[1];

    (0, _qunit.module)(name, {
      beforeEach: function beforeEach() {
        this.application = (0, _wpdaClientTestsHelpersStartApp['default'])();

        if (options.beforeEach) {
          return options.beforeEach.apply(this, arguments);
        }
      },

      afterEach: function afterEach() {
        var _this = this;

        var afterEach = options.afterEach && options.afterEach.apply(this, arguments);
        return Promise.resolve(afterEach).then(function () {
          return (0, _wpdaClientTestsHelpersDestroyApp['default'])(_this.application);
        });
      }
    });
  };
});
define('wpda-client/tests/helpers/module-for-acceptance.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | helpers/module-for-acceptance.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/module-for-acceptance.js should pass jshint.');
  });
});
define('wpda-client/tests/helpers/resolver', ['exports', 'wpda-client/resolver', 'wpda-client/config/environment'], function (exports, _wpdaClientResolver, _wpdaClientConfigEnvironment) {

  var resolver = _wpdaClientResolver['default'].create();

  resolver.namespace = {
    modulePrefix: _wpdaClientConfigEnvironment['default'].modulePrefix,
    podModulePrefix: _wpdaClientConfigEnvironment['default'].podModulePrefix
  };

  exports['default'] = resolver;
});
define('wpda-client/tests/helpers/resolver.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | helpers/resolver.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/resolver.js should pass jshint.');
  });
});
define('wpda-client/tests/helpers/start-app', ['exports', 'ember', 'wpda-client/app', 'wpda-client/config/environment'], function (exports, _ember, _wpdaClientApp, _wpdaClientConfigEnvironment) {
  exports['default'] = startApp;

  function startApp(attrs) {
    var application = undefined;

    var attributes = _ember['default'].merge({}, _wpdaClientConfigEnvironment['default'].APP);
    attributes = _ember['default'].merge(attributes, attrs); // use defaults, but you can override;

    _ember['default'].run(function () {
      application = _wpdaClientApp['default'].create(attributes);
      application.setupForTesting();
      application.injectTestHelpers();
    });

    return application;
  }
});
define('wpda-client/tests/helpers/start-app.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | helpers/start-app.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/start-app.js should pass jshint.');
  });
});
define('wpda-client/tests/mixins/places/save-model-mixin.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | mixins/places/save-model-mixin.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'mixins/places/save-model-mixin.js should pass jshint.');
  });
});
define('wpda-client/tests/models/place.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | models/place.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/place.js should pass jshint.');
  });
});
define('wpda-client/tests/resolver.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | resolver.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'resolver.js should pass jshint.');
  });
});
define('wpda-client/tests/router.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | router.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'router.js should pass jshint.');
  });
});
define('wpda-client/tests/routes/application.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | routes/application.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/application.js should pass jshint.');
  });
});
define('wpda-client/tests/routes/login.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | routes/login.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/login.js should pass jshint.');
  });
});
define('wpda-client/tests/routes/places/edit.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | routes/places/edit.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/places/edit.js should pass jshint.');
  });
});
define('wpda-client/tests/routes/places/index.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | routes/places/index.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/places/index.js should pass jshint.');
  });
});
define('wpda-client/tests/routes/places/new.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | routes/places/new.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/places/new.js should pass jshint.');
  });
});
define('wpda-client/tests/routes/register.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | routes/register.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/register.js should pass jshint.');
  });
});
define('wpda-client/tests/serializers/place.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | serializers/place.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(false, 'serializers/place.js should pass jshint.\nserializers/place.js: line 2, col 8, \'DS\' is defined but never used.\n\n1 error');
  });
});
define('wpda-client/tests/test-helper', ['exports', 'wpda-client/tests/helpers/resolver', 'ember-qunit'], function (exports, _wpdaClientTestsHelpersResolver, _emberQunit) {

  (0, _emberQunit.setResolver)(_wpdaClientTestsHelpersResolver['default']);
});
define('wpda-client/tests/test-helper.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | test-helper.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'test-helper.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/adapters/application-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('adapter:application', 'Unit | Adapter | application', {
    // Specify the other units that are required for this test.
    // needs: ['serializer:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var adapter = this.subject();
    assert.ok(adapter);
  });
});
define('wpda-client/tests/unit/adapters/application-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/adapters/application-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/adapters/application-test.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/controllers/application-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('controller:application', 'Unit | Controller | application', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wpda-client/tests/unit/controllers/application-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/controllers/application-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/application-test.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/controllers/login-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('controller:login', 'Unit | Controller | login', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wpda-client/tests/unit/controllers/login-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/controllers/login-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/login-test.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/controllers/register-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('controller:register', 'Unit | Controller | register', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wpda-client/tests/unit/controllers/register-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/controllers/register-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/register-test.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/routes/application-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('route:application', 'Unit | Route | application', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wpda-client/tests/unit/routes/application-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/routes/application-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/application-test.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/routes/login-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('route:login', 'Unit | Route | login', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wpda-client/tests/unit/routes/login-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/routes/login-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/login-test.js should pass jshint.');
  });
});
define('wpda-client/tests/unit/routes/register-test', ['exports', 'ember-qunit'], function (exports, _emberQunit) {

  (0, _emberQunit.moduleFor)('route:register', 'Unit | Route | register', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wpda-client/tests/unit/routes/register-test.jshint', ['exports'], function (exports) {
  'use strict';

  QUnit.module('JSHint | unit/routes/register-test.js');
  QUnit.test('should pass jshint', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/register-test.js should pass jshint.');
  });
});
/* jshint ignore:start */

require('wpda-client/tests/test-helper');
EmberENV.TESTS_FILE_LOADED = true;

/* jshint ignore:end */
//# sourceMappingURL=tests.map
