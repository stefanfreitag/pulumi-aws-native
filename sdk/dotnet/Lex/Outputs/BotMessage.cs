// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Outputs
{

    /// <summary>
    /// The primary message that Amazon Lex should send to the user.
    /// </summary>
    [OutputType]
    public sealed class BotMessage
    {
        public readonly Outputs.BotCustomPayload? CustomPayload;
        public readonly Outputs.BotImageResponseCard? ImageResponseCard;
        public readonly Outputs.BotPlainTextMessage? PlainTextMessage;
        public readonly Outputs.BotSSMLMessage? SSMLMessage;

        [OutputConstructor]
        private BotMessage(
            Outputs.BotCustomPayload? customPayload,

            Outputs.BotImageResponseCard? imageResponseCard,

            Outputs.BotPlainTextMessage? plainTextMessage,

            Outputs.BotSSMLMessage? sSMLMessage)
        {
            CustomPayload = customPayload;
            ImageResponseCard = imageResponseCard;
            PlainTextMessage = plainTextMessage;
            SSMLMessage = sSMLMessage;
        }
    }
}
