// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53.Outputs
{

    [OutputType]
    public sealed class RecordSetGroupRecordSet
    {
        public readonly Outputs.RecordSetGroupAliasTarget? AliasTarget;
        public readonly Outputs.RecordSetGroupCidrRoutingConfig? CidrRoutingConfig;
        public readonly string? Failover;
        public readonly Outputs.RecordSetGroupGeoLocation? GeoLocation;
        public readonly Outputs.RecordSetGroupGeoProximityLocation? GeoProximityLocation;
        public readonly string? HealthCheckId;
        public readonly string? HostedZoneId;
        public readonly string? HostedZoneName;
        public readonly bool? MultiValueAnswer;
        public readonly string Name;
        public readonly string? Region;
        public readonly ImmutableArray<string> ResourceRecords;
        public readonly string? SetIdentifier;
        public readonly string? Ttl;
        public readonly string Type;
        public readonly int? Weight;

        [OutputConstructor]
        private RecordSetGroupRecordSet(
            Outputs.RecordSetGroupAliasTarget? aliasTarget,

            Outputs.RecordSetGroupCidrRoutingConfig? cidrRoutingConfig,

            string? failover,

            Outputs.RecordSetGroupGeoLocation? geoLocation,

            Outputs.RecordSetGroupGeoProximityLocation? geoProximityLocation,

            string? healthCheckId,

            string? hostedZoneId,

            string? hostedZoneName,

            bool? multiValueAnswer,

            string name,

            string? region,

            ImmutableArray<string> resourceRecords,

            string? setIdentifier,

            string? ttl,

            string type,

            int? weight)
        {
            AliasTarget = aliasTarget;
            CidrRoutingConfig = cidrRoutingConfig;
            Failover = failover;
            GeoLocation = geoLocation;
            GeoProximityLocation = geoProximityLocation;
            HealthCheckId = healthCheckId;
            HostedZoneId = hostedZoneId;
            HostedZoneName = hostedZoneName;
            MultiValueAnswer = multiValueAnswer;
            Name = name;
            Region = region;
            ResourceRecords = resourceRecords;
            SetIdentifier = setIdentifier;
            Ttl = ttl;
            Type = type;
            Weight = weight;
        }
    }
}
