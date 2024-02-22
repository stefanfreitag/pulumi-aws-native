// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dms
{
    public static class GetDataProvider
    {
        /// <summary>
        /// Resource schema for AWS::DMS::DataProvider
        /// </summary>
        public static Task<GetDataProviderResult> InvokeAsync(GetDataProviderArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDataProviderResult>("aws-native:dms:getDataProvider", args ?? new GetDataProviderArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DMS::DataProvider
        /// </summary>
        public static Output<GetDataProviderResult> Invoke(GetDataProviderInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDataProviderResult>("aws-native:dms:getDataProvider", args ?? new GetDataProviderInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDataProviderArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The data provider ARN.
        /// </summary>
        [Input("dataProviderArn", required: true)]
        public string DataProviderArn { get; set; } = null!;

        public GetDataProviderArgs()
        {
        }
        public static new GetDataProviderArgs Empty => new GetDataProviderArgs();
    }

    public sealed class GetDataProviderInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The data provider ARN.
        /// </summary>
        [Input("dataProviderArn", required: true)]
        public Input<string> DataProviderArn { get; set; } = null!;

        public GetDataProviderInvokeArgs()
        {
        }
        public static new GetDataProviderInvokeArgs Empty => new GetDataProviderInvokeArgs();
    }


    [OutputType]
    public sealed class GetDataProviderResult
    {
        /// <summary>
        /// The data provider ARN.
        /// </summary>
        public readonly string? DataProviderArn;
        /// <summary>
        /// The data provider creation time.
        /// </summary>
        public readonly string? DataProviderCreationTime;
        /// <summary>
        /// The property describes a name to identify the data provider.
        /// </summary>
        public readonly string? DataProviderName;
        /// <summary>
        /// The optional description of the data provider.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The property describes a data engine for the data provider.
        /// </summary>
        public readonly Pulumi.AwsNative.Dms.DataProviderEngine? Engine;
        /// <summary>
        /// The property identifies the exact type of settings for the data provider.
        /// </summary>
        public readonly object? Settings;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetDataProviderResult(
            string? dataProviderArn,

            string? dataProviderCreationTime,

            string? dataProviderName,

            string? description,

            Pulumi.AwsNative.Dms.DataProviderEngine? engine,

            object? settings,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            DataProviderArn = dataProviderArn;
            DataProviderCreationTime = dataProviderCreationTime;
            DataProviderName = dataProviderName;
            Description = description;
            Engine = engine;
            Settings = settings;
            Tags = tags;
        }
    }
}
