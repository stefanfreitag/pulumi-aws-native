// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Neptune.Outputs
{

    /// <summary>
    /// Contains the scaling configuration of an Neptune Serverless DB cluster.
    /// </summary>
    [OutputType]
    public sealed class DBClusterServerlessScalingConfiguration
    {
        /// <summary>
        /// The maximum number of Neptune capacity units (NCUs) for a DB instance in an Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 40, 40.5, 41, and so on. The smallest value you can use is 2.5, whereas the largest is 128.
        /// </summary>
        public readonly double MaxCapacity;
        /// <summary>
        /// The minimum number of Neptune capacity units (NCUs) for a DB instance in an Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 8, 8.5, 9, and so on. The smallest value you can use is 1, whereas the largest is 128.
        /// </summary>
        public readonly double MinCapacity;

        [OutputConstructor]
        private DBClusterServerlessScalingConfiguration(
            double maxCapacity,

            double minCapacity)
        {
            MaxCapacity = maxCapacity;
            MinCapacity = minCapacity;
        }
    }
}
