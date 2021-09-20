// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Outputs
{

    [OutputType]
    public sealed class DataSourceDataSourceVpcConfiguration
    {
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly ImmutableArray<string> SubnetIds;

        [OutputConstructor]
        private DataSourceDataSourceVpcConfiguration(
            ImmutableArray<string> securityGroupIds,

            ImmutableArray<string> subnetIds)
        {
            SecurityGroupIds = securityGroupIds;
            SubnetIds = subnetIds;
        }
    }
}
