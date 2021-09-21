// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticBeanstalk.Outputs
{

    [OutputType]
    public sealed class EnvironmentTier
    {
        public readonly string? Name;
        public readonly string? Type;
        public readonly string? Version;

        [OutputConstructor]
        private EnvironmentTier(
            string? name,

            string? type,

            string? version)
        {
            Name = name;
            Type = type;
            Version = version;
        }
    }
}
