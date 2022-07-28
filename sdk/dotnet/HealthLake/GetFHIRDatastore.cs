// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.HealthLake
{
    public static class GetFHIRDatastore
    {
        /// <summary>
        /// HealthLake FHIR Datastore
        /// </summary>
        public static Task<GetFHIRDatastoreResult> InvokeAsync(GetFHIRDatastoreArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetFHIRDatastoreResult>("aws-native:healthlake:getFHIRDatastore", args ?? new GetFHIRDatastoreArgs(), options.WithDefaults());

        /// <summary>
        /// HealthLake FHIR Datastore
        /// </summary>
        public static Output<GetFHIRDatastoreResult> Invoke(GetFHIRDatastoreInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetFHIRDatastoreResult>("aws-native:healthlake:getFHIRDatastore", args ?? new GetFHIRDatastoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFHIRDatastoreArgs : global::Pulumi.InvokeArgs
    {
        [Input("datastoreId", required: true)]
        public string DatastoreId { get; set; } = null!;

        public GetFHIRDatastoreArgs()
        {
        }
        public static new GetFHIRDatastoreArgs Empty => new GetFHIRDatastoreArgs();
    }

    public sealed class GetFHIRDatastoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("datastoreId", required: true)]
        public Input<string> DatastoreId { get; set; } = null!;

        public GetFHIRDatastoreInvokeArgs()
        {
        }
        public static new GetFHIRDatastoreInvokeArgs Empty => new GetFHIRDatastoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetFHIRDatastoreResult
    {
        public readonly Outputs.FHIRDatastoreCreatedAt? CreatedAt;
        public readonly string? DatastoreArn;
        public readonly string? DatastoreEndpoint;
        public readonly string? DatastoreId;
        public readonly Pulumi.AwsNative.HealthLake.FHIRDatastoreDatastoreStatus? DatastoreStatus;
        public readonly ImmutableArray<Outputs.FHIRDatastoreTag> Tags;

        [OutputConstructor]
        private GetFHIRDatastoreResult(
            Outputs.FHIRDatastoreCreatedAt? createdAt,

            string? datastoreArn,

            string? datastoreEndpoint,

            string? datastoreId,

            Pulumi.AwsNative.HealthLake.FHIRDatastoreDatastoreStatus? datastoreStatus,

            ImmutableArray<Outputs.FHIRDatastoreTag> tags)
        {
            CreatedAt = createdAt;
            DatastoreArn = datastoreArn;
            DatastoreEndpoint = datastoreEndpoint;
            DatastoreId = datastoreId;
            DatastoreStatus = datastoreStatus;
            Tags = tags;
        }
    }
}
