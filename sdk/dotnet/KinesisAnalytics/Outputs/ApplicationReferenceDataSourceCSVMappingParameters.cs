// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalytics.Outputs
{

    [OutputType]
    public sealed class ApplicationReferenceDataSourceCSVMappingParameters
    {
        public readonly string RecordColumnDelimiter;
        public readonly string RecordRowDelimiter;

        [OutputConstructor]
        private ApplicationReferenceDataSourceCSVMappingParameters(
            string recordColumnDelimiter,

            string recordRowDelimiter)
        {
            RecordColumnDelimiter = recordColumnDelimiter;
            RecordRowDelimiter = recordRowDelimiter;
        }
    }
}
