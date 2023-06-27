// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.GroundStation
{
    [EnumType]
    public readonly struct ConfigBandwidthUnits : IEquatable<ConfigBandwidthUnits>
    {
        private readonly string _value;

        private ConfigBandwidthUnits(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConfigBandwidthUnits GHz { get; } = new ConfigBandwidthUnits("GHz");
        public static ConfigBandwidthUnits MHz { get; } = new ConfigBandwidthUnits("MHz");
        public static ConfigBandwidthUnits KHz { get; } = new ConfigBandwidthUnits("kHz");

        public static bool operator ==(ConfigBandwidthUnits left, ConfigBandwidthUnits right) => left.Equals(right);
        public static bool operator !=(ConfigBandwidthUnits left, ConfigBandwidthUnits right) => !left.Equals(right);

        public static explicit operator string(ConfigBandwidthUnits value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConfigBandwidthUnits other && Equals(other);
        public bool Equals(ConfigBandwidthUnits other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConfigEirpUnits : IEquatable<ConfigEirpUnits>
    {
        private readonly string _value;

        private ConfigEirpUnits(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConfigEirpUnits DBW { get; } = new ConfigEirpUnits("dBW");

        public static bool operator ==(ConfigEirpUnits left, ConfigEirpUnits right) => left.Equals(right);
        public static bool operator !=(ConfigEirpUnits left, ConfigEirpUnits right) => !left.Equals(right);

        public static explicit operator string(ConfigEirpUnits value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConfigEirpUnits other && Equals(other);
        public bool Equals(ConfigEirpUnits other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConfigFrequencyUnits : IEquatable<ConfigFrequencyUnits>
    {
        private readonly string _value;

        private ConfigFrequencyUnits(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConfigFrequencyUnits GHz { get; } = new ConfigFrequencyUnits("GHz");
        public static ConfigFrequencyUnits MHz { get; } = new ConfigFrequencyUnits("MHz");
        public static ConfigFrequencyUnits KHz { get; } = new ConfigFrequencyUnits("kHz");

        public static bool operator ==(ConfigFrequencyUnits left, ConfigFrequencyUnits right) => left.Equals(right);
        public static bool operator !=(ConfigFrequencyUnits left, ConfigFrequencyUnits right) => !left.Equals(right);

        public static explicit operator string(ConfigFrequencyUnits value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConfigFrequencyUnits other && Equals(other);
        public bool Equals(ConfigFrequencyUnits other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConfigPolarization : IEquatable<ConfigPolarization>
    {
        private readonly string _value;

        private ConfigPolarization(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConfigPolarization LeftHand { get; } = new ConfigPolarization("LEFT_HAND");
        public static ConfigPolarization RightHand { get; } = new ConfigPolarization("RIGHT_HAND");
        public static ConfigPolarization None { get; } = new ConfigPolarization("NONE");

        public static bool operator ==(ConfigPolarization left, ConfigPolarization right) => left.Equals(right);
        public static bool operator !=(ConfigPolarization left, ConfigPolarization right) => !left.Equals(right);

        public static explicit operator string(ConfigPolarization value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConfigPolarization other && Equals(other);
        public bool Equals(ConfigPolarization other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConfigTrackingConfigAutotrack : IEquatable<ConfigTrackingConfigAutotrack>
    {
        private readonly string _value;

        private ConfigTrackingConfigAutotrack(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConfigTrackingConfigAutotrack Required { get; } = new ConfigTrackingConfigAutotrack("REQUIRED");
        public static ConfigTrackingConfigAutotrack Preferred { get; } = new ConfigTrackingConfigAutotrack("PREFERRED");
        public static ConfigTrackingConfigAutotrack Removed { get; } = new ConfigTrackingConfigAutotrack("REMOVED");

        public static bool operator ==(ConfigTrackingConfigAutotrack left, ConfigTrackingConfigAutotrack right) => left.Equals(right);
        public static bool operator !=(ConfigTrackingConfigAutotrack left, ConfigTrackingConfigAutotrack right) => !left.Equals(right);

        public static explicit operator string(ConfigTrackingConfigAutotrack value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConfigTrackingConfigAutotrack other && Equals(other);
        public bool Equals(ConfigTrackingConfigAutotrack other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The status of AgentEndpoint.
    /// </summary>
    [EnumType]
    public readonly struct DataflowEndpointGroupAgentStatus : IEquatable<DataflowEndpointGroupAgentStatus>
    {
        private readonly string _value;

        private DataflowEndpointGroupAgentStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DataflowEndpointGroupAgentStatus Success { get; } = new DataflowEndpointGroupAgentStatus("SUCCESS");
        public static DataflowEndpointGroupAgentStatus Failed { get; } = new DataflowEndpointGroupAgentStatus("FAILED");
        public static DataflowEndpointGroupAgentStatus Active { get; } = new DataflowEndpointGroupAgentStatus("ACTIVE");
        public static DataflowEndpointGroupAgentStatus Inactive { get; } = new DataflowEndpointGroupAgentStatus("INACTIVE");

        public static bool operator ==(DataflowEndpointGroupAgentStatus left, DataflowEndpointGroupAgentStatus right) => left.Equals(right);
        public static bool operator !=(DataflowEndpointGroupAgentStatus left, DataflowEndpointGroupAgentStatus right) => !left.Equals(right);

        public static explicit operator string(DataflowEndpointGroupAgentStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DataflowEndpointGroupAgentStatus other && Equals(other);
        public bool Equals(DataflowEndpointGroupAgentStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The results of the audit.
    /// </summary>
    [EnumType]
    public readonly struct DataflowEndpointGroupAuditResults : IEquatable<DataflowEndpointGroupAuditResults>
    {
        private readonly string _value;

        private DataflowEndpointGroupAuditResults(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DataflowEndpointGroupAuditResults Healthy { get; } = new DataflowEndpointGroupAuditResults("HEALTHY");
        public static DataflowEndpointGroupAuditResults Unhealthy { get; } = new DataflowEndpointGroupAuditResults("UNHEALTHY");

        public static bool operator ==(DataflowEndpointGroupAuditResults left, DataflowEndpointGroupAuditResults right) => left.Equals(right);
        public static bool operator !=(DataflowEndpointGroupAuditResults left, DataflowEndpointGroupAuditResults right) => !left.Equals(right);

        public static explicit operator string(DataflowEndpointGroupAuditResults value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DataflowEndpointGroupAuditResults other && Equals(other);
        public bool Equals(DataflowEndpointGroupAuditResults other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
