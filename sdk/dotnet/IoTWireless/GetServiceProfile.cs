// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless
{
    public static class GetServiceProfile
    {
        /// <summary>
        /// An example resource schema demonstrating some basic constructs and validation rules.
        /// </summary>
        public static Task<GetServiceProfileResult> InvokeAsync(GetServiceProfileArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServiceProfileResult>("aws-native:iotwireless:getServiceProfile", args ?? new GetServiceProfileArgs(), options.WithDefaults());

        /// <summary>
        /// An example resource schema demonstrating some basic constructs and validation rules.
        /// </summary>
        public static Output<GetServiceProfileResult> Invoke(GetServiceProfileInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServiceProfileResult>("aws-native:iotwireless:getServiceProfile", args ?? new GetServiceProfileInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServiceProfileArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Service profile Id. Returned after successful create.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetServiceProfileArgs()
        {
        }
        public static new GetServiceProfileArgs Empty => new GetServiceProfileArgs();
    }

    public sealed class GetServiceProfileInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Service profile Id. Returned after successful create.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetServiceProfileInvokeArgs()
        {
        }
        public static new GetServiceProfileInvokeArgs Empty => new GetServiceProfileInvokeArgs();
    }


    [OutputType]
    public sealed class GetServiceProfileResult
    {
        /// <summary>
        /// Service profile Arn. Returned after successful create.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Service profile Id. Returned after successful create.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
        /// </summary>
        public readonly Outputs.ServiceProfileLoRaWANServiceProfile? LoRaWAN;
        /// <summary>
        /// Name of service profile
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// A list of key-value pairs that contain metadata for the service profile.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServiceProfileTag> Tags;

        [OutputConstructor]
        private GetServiceProfileResult(
            string? arn,

            string? id,

            Outputs.ServiceProfileLoRaWANServiceProfile? loRaWAN,

            string? name,

            ImmutableArray<Outputs.ServiceProfileTag> tags)
        {
            Arn = arn;
            Id = id;
            LoRaWAN = loRaWAN;
            Name = name;
            Tags = tags;
        }
    }
}
