"""Automated Test Suite for Cloud Fleet Orchestrator (Module 05 Capstone Project).

Verifies that all 6 core Object-Oriented Programming concepts are properly implemented:
1. Dataclasses & Validation
2. Composition & Dependency Injection
3. Encapsulation & Properties (@property, @setter, validation)
4. Abstract Base Classes & Inheritance
5. Polymorphism & Method Overriding
6. Magic (Dunder) Methods
"""

import sys
from fleet_orchestrator import (
    CPU,
    BaseServer,
    DatabaseServer,
    ServerCluster,
    Storage,
    TaskReport,
    WebServer,
)


def run_tests():
    print("=" * 60)
    print("  RUNNING AUTOMATED TESTS: CLOUD FLEET ORCHESTRATOR")
    print("=" * 60)
    passed_count = 0
    total_tests = 7

    # -------------------------------------------------------------
    # Test 1: Modern Data Classes (@dataclass, __post_init__)
    # -------------------------------------------------------------
    try:
        report = TaskReport(
            task_name="Backup",
            server_hostname="db-01",
            status="SUCCESS",
            duration_ms=120.5,
        )
        assert report.task_name == "Backup", "TaskReport task_name mismatch"
        assert report.timestamp is not None, "TaskReport timestamp should have default value"

        # Verify post_init negative duration validation
        try:
            TaskReport("Fail", "srv-1", "ERR", duration_ms=-10.0)
            raise AssertionError("TaskReport allowed negative duration_ms without raising ValueError")
        except ValueError:
            pass  # Expected

        passed_count += 1
        print("✅ [1/7] Data Classes & Post-Init Validation: PASSED")
    except Exception as e:
        print(f"❌ [1/7] Data Classes: FAILED -> {e}")

    # -------------------------------------------------------------
    # Test 2: Composition & Component Injection
    # -------------------------------------------------------------
    try:
        cpu = CPU(model="Apple M3 Pro", cores=12)
        storage = Storage(capacity_gb=1000, storage_type="PCIe SSD")
        server = WebServer("test-web", "10.0.0.1", cpu=cpu, storage=storage)

        assert server.cpu.model == "Apple M3 Pro", "CPU component model mismatch"
        assert server.storage.capacity_gb == 1000, "Storage component capacity mismatch"
        assert "12 Cores" in str(server.cpu), "CPU __str__ failed"

        passed_count += 1
        print("✅ [2/7] Composition (HAS-A Relationship): PASSED")
    except Exception as e:
        print(f"❌ [2/7] Composition: FAILED -> {e}")

    # -------------------------------------------------------------
    # Test 3: Abstract Base Class Enforcement
    # -------------------------------------------------------------
    try:
        # BaseServer is abstract; direct instantiation must raise TypeError
        try:
            BaseServer("raw-srv", "10.0.0.99", cpu, storage)
            raise AssertionError("BaseServer was instantiated directly; it must be an Abstract Base Class (ABC)")
        except TypeError:
            pass  # Expected behavior for ABCs

        passed_count += 1
        print("✅ [3/7] Abstract Base Class (ABC) Contract Enforcement: PASSED")
    except Exception as e:
        print(f"❌ [3/7] Abstract Base Class: FAILED -> {e}")

    # -------------------------------------------------------------
    # Test 4: Encapsulation & Properties (@property, @setter, computed)
    # -------------------------------------------------------------
    try:
        server = WebServer("sec-web", "10.0.0.2", cpu, storage)
        server.cpu_usage = 50.0
        assert server.cpu_usage == 50.0, "Getter failed to return cpu_usage"
        assert server.is_overloaded is False, "Server should not be overloaded at 50% CPU"

        server.cpu_usage = 95.0
        assert server.is_overloaded is True, "Server should be overloaded at 95% CPU"

        # Verify validation prevents out-of-range values
        try:
            server.cpu_usage = 105.0
            raise AssertionError("Setter allowed CPU > 100% without raising ValueError")
        except ValueError:
            pass

        try:
            server.cpu_usage = -5.0
            raise AssertionError("Setter allowed CPU < 0% without raising ValueError")
        except ValueError:
            pass

        passed_count += 1
        print("✅ [4/7] Encapsulation, Validation & Computed Properties: PASSED")
    except Exception as e:
        print(f"❌ [4/7] Encapsulation: FAILED -> {e}")

    # -------------------------------------------------------------
    # Test 5: Class Attributes, Class Methods & Static Methods
    # -------------------------------------------------------------
    try:
        # Static method test
        assert BaseServer.is_valid_ipv4("192.168.1.1") is True, "Static method failed valid IP"
        assert BaseServer.is_valid_ipv4("999.1.1.1") is False, "Static method allowed invalid IP octet"
        assert BaseServer.is_valid_ipv4("invalid-ip") is False, "Static method allowed non-numeric IP"

        # Class method factory test
        csv_server = WebServer.from_csv_string("factory-node,10.10.1.1,16,1000")
        assert csv_server.hostname == "factory-node", "Factory method hostname mismatch"
        assert csv_server.cpu.cores == 16, "Factory method CPU cores mismatch"
        assert csv_server.storage.capacity_gb == 1000, "Factory method storage mismatch"

        # Class attribute check
        assert BaseServer.total_servers_created > 0, "Class attribute total_servers_created failed to increment"

        passed_count += 1
        print("✅ [5/7] Class Attributes, Class Methods & Static Methods: PASSED")
    except Exception as e:
        print(f"❌ [5/7] Class & Static Methods: FAILED -> {e}")

    # -------------------------------------------------------------
    # Test 6: Inheritance & Polymorphism (Dynamic Dispatch)
    # -------------------------------------------------------------
    try:
        web = WebServer("web-poly", "10.0.0.10", cpu, storage, ssl_enabled=True)
        db = DatabaseServer("db-poly", "10.0.0.20", cpu, storage)

        servers = [web, db]
        reports = [s.handle_request("test/endpoint") for s in servers]

        assert "HTTPS" in reports[0].task_name, "WebServer failed to handle request polymorphically"
        assert "SQL QUERY" in reports[1].task_name, "DatabaseServer failed to handle request polymorphically"

        passed_count += 1
        print("✅ [6/7] Inheritance & Polymorphism (Method Overriding): PASSED")
    except Exception as e:
        print(f"❌ [6/7] Inheritance & Polymorphism: FAILED -> {e}")

    # -------------------------------------------------------------
    # Test 7: Magic Methods (__len__, __getitem__, __contains__, __add__, __eq__)
    # -------------------------------------------------------------
    try:
        s1 = WebServer("node-1", "10.0.0.31", cpu, storage)
        s2 = DatabaseServer("node-2", "10.0.0.32", cpu, storage)
        s3 = WebServer("node-3", "10.0.0.33", cpu, storage)

        # __eq__ test
        clone_s1 = WebServer("node-1", "10.0.0.31", cpu, storage)
        assert s1 == clone_s1, "__eq__ failed for identical servers"
        assert s1 != s2, "__eq__ failed for distinct servers"

        # ServerCluster container tests
        cluster = ServerCluster("TestCluster", [s1, s2])

        # __len__
        assert len(cluster) == 2, "__len__ failed on ServerCluster"

        # __getitem__
        assert cluster[0] == s1, "__getitem__ failed for index 0"
        assert cluster[1] == s2, "__getitem__ failed for index 1"

        # __contains__
        assert s1 in cluster, "__contains__ failed for object lookup"
        assert "node-2" in cluster, "__contains__ failed for string hostname lookup"
        assert "unknown-node" not in cluster, "__contains__ returned True for missing node"

        # __add__ with server
        merged_cluster = cluster + s3
        assert len(merged_cluster) == 3, "__add__ with server failed"
        assert s3 in merged_cluster, "__add__ did not include new server"

        # __add__ with another cluster
        s4 = DatabaseServer("node-4", "10.0.0.34", cpu, storage)
        other_cluster = ServerCluster("ExtraCluster", [s4])
        big_cluster = cluster + other_cluster
        assert len(big_cluster) == 3, "__add__ with another cluster failed"

        passed_count += 1
        print("✅ [7/7] Magic (Dunder) Methods & Container Emulation: PASSED")
    except Exception as e:
        print(f"❌ [7/7] Magic Methods: FAILED -> {e}")

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------
    print("=" * 60)
    if passed_count == total_tests:
        print(f"🎉 ALL {total_tests} OOP TEST SUITES PASSED PERFECTLY!")
        print("=" * 60)
        return 0
    else:
        print(f"⚠️  {passed_count}/{total_tests} TESTS PASSED. PLEASE REVIEW FAILURES.")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
