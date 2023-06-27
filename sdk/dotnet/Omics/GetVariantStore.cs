// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Omics
{
    public static class GetVariantStore
    {
        /// <summary>
        /// Definition of AWS::Omics::VariantStore Resource Type
        /// </summary>
        public static Task<GetVariantStoreResult> InvokeAsync(GetVariantStoreArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVariantStoreResult>("aws-native:omics:getVariantStore", args ?? new GetVariantStoreArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::Omics::VariantStore Resource Type
        /// </summary>
        public static Output<GetVariantStoreResult> Invoke(GetVariantStoreInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVariantStoreResult>("aws-native:omics:getVariantStore", args ?? new GetVariantStoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVariantStoreArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetVariantStoreArgs()
        {
        }
        public static new GetVariantStoreArgs Empty => new GetVariantStoreArgs();
    }

    public sealed class GetVariantStoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetVariantStoreInvokeArgs()
        {
        }
        public static new GetVariantStoreInvokeArgs Empty => new GetVariantStoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetVariantStoreResult
    {
        public readonly string? CreationTime;
        public readonly string? Description;
        public readonly string? Id;
        public readonly Pulumi.AwsNative.Omics.VariantStoreStoreStatus? Status;
        public readonly string? StatusMessage;
        public readonly string? StoreArn;
        public readonly double? StoreSizeBytes;
        public readonly string? UpdateTime;

        [OutputConstructor]
        private GetVariantStoreResult(
            string? creationTime,

            string? description,

            string? id,

            Pulumi.AwsNative.Omics.VariantStoreStoreStatus? status,

            string? statusMessage,

            string? storeArn,

            double? storeSizeBytes,

            string? updateTime)
        {
            CreationTime = creationTime;
            Description = description;
            Id = id;
            Status = status;
            StatusMessage = statusMessage;
            StoreArn = storeArn;
            StoreSizeBytes = storeSizeBytes;
            UpdateTime = updateTime;
        }
    }
}
