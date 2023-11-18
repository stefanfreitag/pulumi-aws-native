// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Outputs
{

    /// <summary>
    /// The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
    /// </summary>
    [OutputType]
    public sealed class DataRepositoryAssociationS3
    {
        /// <summary>
        /// Describes a data repository association's automatic export policy. The ``AutoExportPolicy`` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.
        ///  The ``AutoExportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        /// </summary>
        public readonly Outputs.DataRepositoryAssociationAutoExportPolicy? AutoExportPolicy;
        /// <summary>
        /// Describes the data repository association's automatic import policy. The AutoImportPolicy defines how Amazon FSx keeps your file metadata and directory listings up to date by importing changes to your Amazon FSx for Lustre file system as you modify objects in a linked S3 bucket.
        ///  The ``AutoImportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        /// </summary>
        public readonly Outputs.DataRepositoryAssociationAutoImportPolicy? AutoImportPolicy;

        [OutputConstructor]
        private DataRepositoryAssociationS3(
            Outputs.DataRepositoryAssociationAutoExportPolicy? autoExportPolicy,

            Outputs.DataRepositoryAssociationAutoImportPolicy? autoImportPolicy)
        {
            AutoExportPolicy = autoExportPolicy;
            AutoImportPolicy = autoImportPolicy;
        }
    }
}
