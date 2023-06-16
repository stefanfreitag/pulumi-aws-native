// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms.Outputs
{

    [OutputType]
    public sealed class CollaborationDataEncryptionMetadata
    {
        public readonly bool AllowCleartext;
        public readonly bool AllowDuplicates;
        public readonly bool AllowJoinsOnColumnsWithDifferentNames;
        public readonly bool PreserveNulls;

        [OutputConstructor]
        private CollaborationDataEncryptionMetadata(
            bool allowCleartext,

            bool allowDuplicates,

            bool allowJoinsOnColumnsWithDifferentNames,

            bool preserveNulls)
        {
            AllowCleartext = allowCleartext;
            AllowDuplicates = allowDuplicates;
            AllowJoinsOnColumnsWithDifferentNames = allowJoinsOnColumnsWithDifferentNames;
            PreserveNulls = preserveNulls;
        }
    }
}
