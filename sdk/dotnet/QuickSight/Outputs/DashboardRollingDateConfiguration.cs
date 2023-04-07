// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class DashboardRollingDateConfiguration
    {
        public readonly string? DataSetIdentifier;
        public readonly string Expression;

        [OutputConstructor]
        private DashboardRollingDateConfiguration(
            string? dataSetIdentifier,

            string expression)
        {
            DataSetIdentifier = dataSetIdentifier;
            Expression = expression;
        }
    }
}
