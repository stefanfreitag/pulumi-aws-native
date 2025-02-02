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
    /// Contains information about code hooks that Amazon Lex calls during a conversation.
    /// </summary>
    [OutputType]
    public sealed class BotAliasConversationLogSettings
    {
        public readonly ImmutableArray<Outputs.BotAliasAudioLogSetting> AudioLogSettings;
        public readonly ImmutableArray<Outputs.BotAliasTextLogSetting> TextLogSettings;

        [OutputConstructor]
        private BotAliasConversationLogSettings(
            ImmutableArray<Outputs.BotAliasAudioLogSetting> audioLogSettings,

            ImmutableArray<Outputs.BotAliasTextLogSetting> textLogSettings)
        {
            AudioLogSettings = audioLogSettings;
            TextLogSettings = textLogSettings;
        }
    }
}
