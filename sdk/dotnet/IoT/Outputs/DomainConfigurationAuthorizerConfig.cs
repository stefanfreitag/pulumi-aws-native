// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Outputs
{

    [OutputType]
    public sealed class DomainConfigurationAuthorizerConfig
    {
        public readonly bool? AllowAuthorizerOverride;
        public readonly string? DefaultAuthorizerName;

        [OutputConstructor]
        private DomainConfigurationAuthorizerConfig(
            bool? allowAuthorizerOverride,

            string? defaultAuthorizerName)
        {
            AllowAuthorizerOverride = allowAuthorizerOverride;
            DefaultAuthorizerName = defaultAuthorizerName;
        }
    }
}
