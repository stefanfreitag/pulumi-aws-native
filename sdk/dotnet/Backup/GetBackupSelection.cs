// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup
{
    public static class GetBackupSelection
    {
        /// <summary>
        /// Resource Type definition for AWS::Backup::BackupSelection
        /// </summary>
        public static Task<GetBackupSelectionResult> InvokeAsync(GetBackupSelectionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBackupSelectionResult>("aws-native:backup:getBackupSelection", args ?? new GetBackupSelectionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Backup::BackupSelection
        /// </summary>
        public static Output<GetBackupSelectionResult> Invoke(GetBackupSelectionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetBackupSelectionResult>("aws-native:backup:getBackupSelection", args ?? new GetBackupSelectionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBackupSelectionArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetBackupSelectionArgs()
        {
        }
        public static new GetBackupSelectionArgs Empty => new GetBackupSelectionArgs();
    }

    public sealed class GetBackupSelectionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetBackupSelectionInvokeArgs()
        {
        }
        public static new GetBackupSelectionInvokeArgs Empty => new GetBackupSelectionInvokeArgs();
    }


    [OutputType]
    public sealed class GetBackupSelectionResult
    {
        public readonly string? Id;
        public readonly string? SelectionId;

        [OutputConstructor]
        private GetBackupSelectionResult(
            string? id,

            string? selectionId)
        {
            Id = id;
            SelectionId = selectionId;
        }
    }
}
