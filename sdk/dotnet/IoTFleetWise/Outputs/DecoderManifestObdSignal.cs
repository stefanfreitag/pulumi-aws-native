// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Outputs
{

    [OutputType]
    public sealed class DecoderManifestObdSignal
    {
        public readonly int? BitMaskLength;
        public readonly int? BitRightShift;
        public readonly int ByteLength;
        public readonly double Offset;
        public readonly int Pid;
        public readonly int PidResponseLength;
        public readonly double Scaling;
        public readonly int ServiceMode;
        public readonly int StartByte;

        [OutputConstructor]
        private DecoderManifestObdSignal(
            int? bitMaskLength,

            int? bitRightShift,

            int byteLength,

            double offset,

            int pid,

            int pidResponseLength,

            double scaling,

            int serviceMode,

            int startByte)
        {
            BitMaskLength = bitMaskLength;
            BitRightShift = bitRightShift;
            ByteLength = byteLength;
            Offset = offset;
            Pid = pid;
            PidResponseLength = pidResponseLength;
            Scaling = scaling;
            ServiceMode = serviceMode;
            StartByte = startByte;
        }
    }
}
