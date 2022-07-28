// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless
{
    public static class GetWirelessDevice
    {
        /// <summary>
        /// Create and manage wireless gateways, including LoRa gateways.
        /// </summary>
        public static Task<GetWirelessDeviceResult> InvokeAsync(GetWirelessDeviceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWirelessDeviceResult>("aws-native:iotwireless:getWirelessDevice", args ?? new GetWirelessDeviceArgs(), options.WithDefaults());

        /// <summary>
        /// Create and manage wireless gateways, including LoRa gateways.
        /// </summary>
        public static Output<GetWirelessDeviceResult> Invoke(GetWirelessDeviceInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetWirelessDeviceResult>("aws-native:iotwireless:getWirelessDevice", args ?? new GetWirelessDeviceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWirelessDeviceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Wireless device Id. Returned after successful create.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetWirelessDeviceArgs()
        {
        }
        public static new GetWirelessDeviceArgs Empty => new GetWirelessDeviceArgs();
    }

    public sealed class GetWirelessDeviceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Wireless device Id. Returned after successful create.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetWirelessDeviceInvokeArgs()
        {
        }
        public static new GetWirelessDeviceInvokeArgs Empty => new GetWirelessDeviceInvokeArgs();
    }


    [OutputType]
    public sealed class GetWirelessDeviceResult
    {
        /// <summary>
        /// Wireless device arn. Returned after successful create.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Wireless device description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Wireless device destination name
        /// </summary>
        public readonly string? DestinationName;
        /// <summary>
        /// Wireless device Id. Returned after successful create.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The date and time when the most recent uplink was received.
        /// </summary>
        public readonly string? LastUplinkReceivedAt;
        /// <summary>
        /// The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.
        /// </summary>
        public readonly Outputs.WirelessDeviceLoRaWANDevice? LoRaWAN;
        /// <summary>
        /// Wireless device name
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.
        /// </summary>
        public readonly ImmutableArray<Outputs.WirelessDeviceTag> Tags;
        /// <summary>
        /// Thing arn. Passed into update to associate Thing with Wireless device.
        /// </summary>
        public readonly string? ThingArn;
        /// <summary>
        /// Thing Arn. If there is a Thing created, this can be returned with a Get call.
        /// </summary>
        public readonly string? ThingName;
        /// <summary>
        /// Wireless device type, currently only Sidewalk and LoRa
        /// </summary>
        public readonly Pulumi.AwsNative.IoTWireless.WirelessDeviceType? Type;

        [OutputConstructor]
        private GetWirelessDeviceResult(
            string? arn,

            string? description,

            string? destinationName,

            string? id,

            string? lastUplinkReceivedAt,

            Outputs.WirelessDeviceLoRaWANDevice? loRaWAN,

            string? name,

            ImmutableArray<Outputs.WirelessDeviceTag> tags,

            string? thingArn,

            string? thingName,

            Pulumi.AwsNative.IoTWireless.WirelessDeviceType? type)
        {
            Arn = arn;
            Description = description;
            DestinationName = destinationName;
            Id = id;
            LastUplinkReceivedAt = lastUplinkReceivedAt;
            LoRaWAN = loRaWAN;
            Name = name;
            Tags = tags;
            ThingArn = thingArn;
            ThingName = thingName;
            Type = type;
        }
    }
}
